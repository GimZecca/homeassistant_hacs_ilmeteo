"""Integrazione ilMeteo.it per Home Assistant."""
from __future__ import annotations

import hashlib
import logging
from datetime import datetime, timedelta

import async_timeout
import xmltodict

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .const import BASE_URL, DOMAIN, UPDATE_INTERVAL_MINUTES, WS_VERSION, WS_X_KEY

_LOGGER = logging.getLogger(__name__)

PLATFORMS = [Platform.WEATHER, Platform.SENSOR]


def _compute_x(method: str) -> str:
    """Calcola il token giornaliero: MD5(method + WS_X_KEY + dayOfMonth)."""
    day = datetime.now().strftime("%d")
    return hashlib.md5(f"{method}{WS_X_KEY}{day}".encode()).hexdigest()


async def async_fetch_data(hass: HomeAssistant, location_id: int) -> dict:
    """Scarica e parsa i dati meteo da ilMeteo per un dato ID località."""
    session = async_get_clientsession(hass)
    method = "situationAndForecast"
    params = {
        "force_3h": "0",
        "id":       str(location_id),
        "lang":     "ita",
        "method":   method,
        "type":     "10",
        "v":        WS_VERSION,
        "x":        _compute_x(method),
    }
    try:
        async with async_timeout.timeout(15):
            resp = await session.get(BASE_URL, params=params)
            resp.raise_for_status()
            text = await resp.text(encoding="utf-8", errors="replace")
    except Exception as err:
        raise UpdateFailed(f"Errore di rete: {err}") from err

    if "ACCESS DENIED" in text.upper():
        raise UpdateFailed("ilMeteo: ACCESS DENIED — token x non valido?")

    try:
        data = xmltodict.parse(text)
    except Exception as err:
        raise UpdateFailed(f"Errore parsing XML: {err}") from err

    return data.get("ilMeteo", {})


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Configura l'integrazione da un config entry."""
    location_id = entry.data["location_id"]

    coordinator = DataUpdateCoordinator(
        hass,
        _LOGGER,
        name=f"ilMeteo {entry.data.get('name', location_id)}",
        update_method=lambda: async_fetch_data(hass, location_id),
        update_interval=timedelta(minutes=UPDATE_INTERVAL_MINUTES),
    )

    await coordinator.async_config_entry_first_refresh()

    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = coordinator
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Rimuove il config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)
    return unload_ok
