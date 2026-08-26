"""Entità Weather per ilMeteo — previsioni orarie e giornaliere."""
from __future__ import annotations

import logging
from datetime import datetime

from homeassistant.components.weather import (
    Forecast,
    WeatherEntity,
    WeatherEntityFeature,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import UnitOfPressure, UnitOfSpeed, UnitOfTemperature
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

# Mappa simbolo diurno ilMeteo (1-24, 4b) → condizione Home Assistant.
CONDITION_MAP: dict[str, str] = {
    "1":   "sunny",
    "2":   "sunny",           # sereno e caldo
    "3":   "partlycloudy",
    "4":   "cloudy",
    "4b":  "cloudy",          # molte nubi
    "5":   "rainy",
    "6":   "snowy-rainy",
    "7":   "snowy",
    "8":   "cloudy",          # coperto
    "9":   "rainy",           # pioggia debole
    "10":  "rainy",
    "11":  "snowy",
    "12":  "snowy-rainy",
    "13":  "lightning-rainy",
    "14":  "fog",
    "15":  "fog",             # foschia
    "16":  "lightning-rainy",
    "17":  "hail",
    "18":  "snowy",           # neve debole
    "19":  "lightning-rainy",
    "20":  "lightning-rainy",
    "21":  "partlycloudy",    # poco nuvoloso e caldo
    "22":  "sunny",           # caldo estremo
    "23":  "partlycloudy",    # nubi sparse e caldo
    "24":  "sunny",
}

# Alcuni simboli diurni hanno una condizione HA diversa di notte
# (es. "sereno" diventa "clear-night" invece di "sunny").
NIGHT_CONDITION_OVERRIDE: dict[str, str] = {
    "1": "clear-night",
}


def _condition_from_simbolo(simbolo: str) -> str:
    """Mappa il simbolo ilMeteo a una condizione HA.

    ilMeteo usa simbolo diurno 1-24 (+4b) e, per la notte, lo stesso
    codice + 100 (es. 121 = versione notturna di 21, 105 = versione
    notturna di 5). Questa funzione normalizza qualsiasi variante
    notturna riconducendola al diurno, così non serve elencare ogni
    combinazione a mano (a differenza dell'elenco statico precedente,
    che copriva solo le varianti osservate empiricamente).
    """
    simbolo = str(simbolo).strip()
    if not simbolo:
        return "exceptional"

    if simbolo.isdigit() and int(simbolo) > 100:
        base = str(int(simbolo) - 100)
        override = NIGHT_CONDITION_OVERRIDE.get(base)
        if override:
            return override
        return CONDITION_MAP.get(base, "exceptional")

    return CONDITION_MAP.get(simbolo, "exceptional")


# ---------- helpers ----------

def _temp(val: str | None) -> float | None:
    try:
        return float(str(val).replace("°C","").replace("°","").replace(",",".").strip())
    except (ValueError, AttributeError):
        return None


def _float(val: str | None) -> float | None:
    try:
        return float(str(val).replace(",",".").strip())
    except (ValueError, AttributeError):
        return None


def _pct(val: str | None) -> float | None:
    try:
        return float(str(val).replace("%","").strip())
    except (ValueError, AttributeError):
        return None


def _pressure(val: str | None) -> float | None:
    try:
        return float(str(val).replace("mb","").strip())
    except (ValueError, AttributeError):
        return None


def _wind_speed(val: str | None) -> float | None:
    """Estrae velocità media da stringhe tipo '6 S km/h' o '7/16 SSW km/h'."""
    try:
        speed = str(val).split()[0]
        if "/" in speed:
            speed = speed.split("/")[0]
        return float(speed)
    except (ValueError, AttributeError, IndexError):
        return None


def _precip_mm(val: str | None) -> float | None:
    """Converte il valore precipitazioni in mm.

    ilMeteo lascia il campo vuoto ("") quando non è prevista pioggia,
    invece di scrivere esplicitamente "0mm". Un campo vuoto viene quindi
    trattato come 0.0 (nessuna precipitazione attesa) e non come dato
    mancante, altrimenti i sensori mostrerebbero "unknown" nei giorni
    di bel tempo invece di "0".
    """
    if val is None:
        return None
    val = str(val).strip()
    if val in ("", "- assenti -"):
        return 0.0
    try:
        return float(val.replace("mm", "").replace(",", ".").strip())
    except ValueError:
        return None


# ---------- setup ----------

async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([IlMeteoWeather(coordinator, entry)])


# ---------- entity ----------

class IlMeteoWeather(CoordinatorEntity, WeatherEntity):
    """Rappresenta il meteo corrente con previsioni orarie e giornaliere."""

    _attr_supported_features = (
        WeatherEntityFeature.FORECAST_HOURLY | WeatherEntityFeature.FORECAST_DAILY
    )
    _attr_native_temperature_unit = UnitOfTemperature.CELSIUS
    _attr_native_wind_speed_unit  = UnitOfSpeed.KILOMETERS_PER_HOUR
    _attr_native_pressure_unit    = UnitOfPressure.HPA

    def __init__(self, coordinator, entry: ConfigEntry) -> None:
        super().__init__(coordinator)
        self._entry = entry
        self._attr_unique_id = f"ilmeteo_{entry.data['location_id']}_weather"
        self._attr_name = entry.data.get("name", "ilMeteo")

    @property
    def _data(self) -> dict:
        return self.coordinator.data or {}

    @property
    def _localita(self) -> dict:
        return self._data.get("localita", {})

    @property
    def _situazione(self) -> dict:
        return self._localita.get("situazione", {})

    @property
    def native_temperature(self) -> float | None:
        return _temp(self._situazione.get("@temperatura"))

    @property
    def humidity(self) -> float | None:
        return _pct(self._situazione.get("@umidita"))

    @property
    def native_pressure(self) -> float | None:
        return _pressure(self._situazione.get("@pressione"))

    @property
    def native_wind_speed(self) -> float | None:
        return _wind_speed(self._situazione.get("@wind"))

    @property
    def wind_bearing(self) -> float | None:
        rt = self._data.get("realtime", {}).get("merged", {})
        return _float(rt.get("@wind_rotation"))

    @property
    def condition(self) -> str | None:
        return _condition_from_simbolo(self._situazione.get("@simbolo", ""))

    async def async_forecast_hourly(self) -> list[Forecast] | None:
        return self._hourly()

    async def async_forecast_daily(self) -> list[Forecast] | None:
        return self._daily()

    def _hourly(self) -> list[Forecast]:
        previsioni = self._data.get("previsione", [])
        if isinstance(previsioni, dict):
            previsioni = [previsioni]

        seen: set[str] = set()
        forecasts: list[Forecast] = []

        for block in previsioni:
            righe = block.get("riga", [])
            if isinstance(righe, dict):
                righe = [righe]
            for r in righe:
                ts = r.get("@import_ts", "")
                if ts in seen:
                    continue
                seen.add(ts)
                try:
                    dt = datetime.fromtimestamp(int(ts)).isoformat()
                except (ValueError, TypeError):
                    continue
                forecasts.append(Forecast(
                    datetime=dt,
                    native_temperature=_temp(r.get("@temperatura")),
                    condition=_condition_from_simbolo(r.get("@simbolo", "")),
                    native_precipitation=_precip_mm(r.get("@precipitazioni_valore")),
                    precipitation_probability=_float(r.get("@precipitazioni_prob")),
                    humidity=_pct(r.get("@umidita")),
                    native_wind_speed=_wind_speed(r.get("@wind")),
                    wind_bearing=_float(r.get("@wind_rotation")),
                ))

        return sorted(forecasts, key=lambda f: f["datetime"])[:48]

    def _daily(self) -> list[Forecast]:
        giorni = self._data.get("giornaliere", {}).get("giorno", [])
        if isinstance(giorni, dict):
            giorni = [giorni]

        forecasts: list[Forecast] = []
        for g in giorni:
            ts = g.get("@import_ts", "")
            try:
                dt = datetime.fromtimestamp(int(ts)).isoformat()
            except (ValueError, TypeError):
                continue
            forecasts.append(Forecast(
                datetime=dt,
                native_temperature=_temp(g.get("@max")),
                native_templow=_temp(g.get("@min")),
                condition=_condition_from_simbolo(g.get("@simbolo", "")),
                native_precipitation=_precip_mm(g.get("@precipitazioni_valore")),
                precipitation_probability=_float(g.get("@attendibilita_prob")),
                native_wind_speed=_wind_speed(g.get("@wind")),
            ))
        return forecasts
