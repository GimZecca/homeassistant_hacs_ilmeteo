"""
Scarica e cachea il database comuni da ilMeteo API (method=getDB, format=csv).

Formato risposta CSV (separatore ';'):
  col 0  = ID
  col 1  = sigla provincia (es. PD, MI, RM)
  col 2  = sigla regione abbreviata (es. LOM, VEN, LAZ)
  col 3  = nazione (es. IT)
  col 4  = nome comune
  col 5  = latitudine
  col 6  = longitudine
  col 7  = altitudine
  col 14 = ID (ripetuto)
  ...
"""
from __future__ import annotations

import hashlib
import logging
from datetime import datetime

import async_timeout

from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.storage import Store

from .const import BASE_URL, STORAGE_KEY_COMUNI, STORAGE_VERSION, WS_VERSION, WS_X_KEY

_LOGGER = logging.getLogger(__name__)

# Cache in memoria condivisa tra tutte le istanze del componente
_COMUNI_CACHE: dict[str, dict] | None = None

REGIONI: dict[str, str] = {
    "PIE": "Piemonte",
    "LOM": "Lombardia",
    "VDA": "Valle d'Aosta",
    "LIG": "Liguria",
    "VEN": "Veneto",
    "FVG": "Friuli Venezia Giulia",
    "EMR": "Emilia Romagna",
    "TOS": "Toscana",
    "UMB": "Umbria",
    "MAR": "Marche",
    "LAZ": "Lazio",
    "ABR": "Abruzzo",
    "MOL": "Molise",
    "CAM": "Campania",
    "PUG": "Puglia",
    "BAS": "Basilicata",
    "CAL": "Calabria",
    "SIC": "Sicilia",
    "SAR": "Sardegna",
    "TAA": "Trentino Alto Adige",
}


def _compute_x(method: str) -> str:
    """Calcola il token giornaliero: MD5(method + WS_X_KEY + dayOfMonth)."""
    day = datetime.now().strftime("%d")
    return hashlib.md5(f"{method}{WS_X_KEY}{day}".encode()).hexdigest()


def _parse_csv(text: str) -> dict[str, dict]:
    """Parsa il CSV restituito da getDB e restituisce un dizionario id→info."""
    comuni: dict[str, dict] = {}
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        parts = line.split(";")
        if len(parts) < 8:
            continue
        try:
            lid     = parts[0].strip()
            prov    = parts[1].strip()
            reg_key = parts[2].strip()
            nome    = parts[4].strip()
            lat     = parts[5].strip()
            lon     = parts[6].strip()
            alt     = parts[7].strip()
            if not lid or not nome:
                continue
            comuni[lid] = {
                "nome":    nome,
                "prov":    prov,
                "regione": REGIONI.get(reg_key, reg_key),
                "lat":     lat,
                "lon":     lon,
                "alt":     alt,
            }
        except (IndexError, ValueError):
            continue
    return comuni


async def async_get_comuni(hass: HomeAssistant) -> dict[str, dict]:
    """Restituisce il dizionario comuni.

    Ordine di priorità:
    1. Cache in memoria (resetata ad ogni riavvio di HA)
    2. Storage persistente su disco (sopravvive ai riavvii)
    3. Download dall'API ilMeteo
    4. Fallback al dizionario statico (comuni_data.py)
    """
    global _COMUNI_CACHE

    if _COMUNI_CACHE:
        return _COMUNI_CACHE

    store = Store(hass, STORAGE_VERSION, STORAGE_KEY_COMUNI)
    stored = await store.async_load()
    if stored and isinstance(stored, dict) and len(stored) > 100:
        _LOGGER.debug("ilMeteo: %d comuni caricati dallo storage locale", len(stored))
        _COMUNI_CACHE = stored
        return _COMUNI_CACHE

    _LOGGER.info("ilMeteo: scarico database comuni dall'API...")
    try:
        session = async_get_clientsession(hass)
        method = "getDB"
        params = {
            "method": method,
            "table":  "localita",
            "format": "csv",
            "v":      WS_VERSION,
            "lang":   "ita",
            "x":      _compute_x(method),
        }
        async with async_timeout.timeout(30):
            resp = await session.get(BASE_URL, params=params)
            resp.raise_for_status()
            text = await resp.text(encoding="utf-8", errors="replace")

        if not text or "ACCESS DENIED" in text.upper():
            raise ValueError("Risposta non valida dall'API")

        comuni = _parse_csv(text)
        if len(comuni) < 100:
            raise ValueError(f"Risposta anomala: solo {len(comuni)} comuni")

        _LOGGER.info("ilMeteo: %d comuni scaricati", len(comuni))
        _COMUNI_CACHE = comuni
        await store.async_save(comuni)
        return comuni

    except Exception as err:
        _LOGGER.warning("ilMeteo: impossibile scaricare comuni (%s). Uso dizionario locale.", err)
        from .comuni_data import COMUNI
        return COMUNI


def search_comuni(comuni: dict[str, dict], query: str, max_results: int = 20) -> list[dict]:
    """Ricerca nei comuni per nome (case-insensitive, substring match).

    I risultati che iniziano con la query vengono mostrati prima.
    """
    q = query.lower().strip()
    results = [
        {
            "id":      lid,
            "nome":    info["nome"],
            "prov":    info["prov"],
            "regione": info["regione"],
            "label":   f"{info['nome']} ({info['prov']}) — {info['regione']}",
        }
        for lid, info in comuni.items()
        if q in info["nome"].lower()
    ]
    results.sort(key=lambda x: (not x["nome"].lower().startswith(q), x["nome"]))
    return results[:max_results]


async def async_invalidate_cache(hass: HomeAssistant) -> None:
    """Forza il re-download del database comuni alla prossima richiesta."""
    global _COMUNI_CACHE
    _COMUNI_CACHE = None
    store = Store(hass, STORAGE_VERSION, STORAGE_KEY_COMUNI)
    await store.async_remove()
