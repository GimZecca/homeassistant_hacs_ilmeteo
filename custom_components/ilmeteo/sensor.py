"""Sensori aggiuntivi per ilMeteo."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorEntityDescription,
    SensorStateClass,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import (
    PERCENTAGE,
    UnitOfPressure,
    UnitOfSpeed,
    UnitOfTemperature,
)
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN
from .weather import (
    _condition_from_simbolo,
    _float,
    _pct,
    _precip_mm,
    _pressure,
    _temp,
    _wind_speed,
)


# ---------- helpers ----------

def _situazione(data: dict, key: str) -> Any:
    return data.get("localita", {}).get("situazione", {}).get(key)


def _descrizione(data: dict) -> str | None:
    desc = data.get("localita", {}).get("situazione", {}).get("descrizione")
    if isinstance(desc, dict):
        return desc.get("#text")
    return desc


def _last_update(data: dict) -> str | None:
    return data.get("localita", {}).get("situazione", {}).get("lastUpdate")


def _giorni(data: dict) -> list[dict]:
    giorni = data.get("giornaliere", {}).get("giorno", [])
    if isinstance(giorni, dict):
        giorni = [giorni]
    return giorni


def _giorno(data: dict, index: int) -> dict:
    """Restituisce il blocco giorno all'indice indicato (0=oggi, 1=domani, ...)."""
    g = _giorni(data)
    return g[index] if len(g) > index else {}


def _oggi(data: dict) -> dict:
    return _giorno(data, 0)


def _domani(data: dict) -> dict:
    return _giorno(data, 1)


def _quota_zero(data: dict) -> int | None:
    previsioni = data.get("previsione", [])
    if isinstance(previsioni, dict):
        previsioni = [previsioni]
    for block in previsioni:
        righe = block.get("riga", [])
        if isinstance(righe, dict):
            righe = [righe]
        for r in righe:
            qz = r.get("@quotazero", "")
            if qz:
                try:
                    return int(str(qz).replace("m", "").strip())
                except ValueError:
                    pass
    return None


# ---------- sensor descriptions ----------

@dataclass
class IlMeteoSensorDescription(SensorEntityDescription):
    value_fn: Callable[[dict], Any] = None
    custom_unit: str | None = None
    custom_icon: str | None = None


SENSORS: list[IlMeteoSensorDescription] = [
    # ---- Condizioni attuali ----
    IlMeteoSensorDescription(
        key="temperatura",
        name="Temperatura",
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        custom_unit=UnitOfTemperature.CELSIUS,
        value_fn=lambda d: _temp(_situazione(d, "@temperatura")),
    ),
    IlMeteoSensorDescription(
        key="percepita",
        name="Temperatura Percepita",
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        custom_unit=UnitOfTemperature.CELSIUS,
        value_fn=lambda d: _temp(_situazione(d, "@percepita")),
    ),
    IlMeteoSensorDescription(
        key="umidita",
        name="Umidità",
        device_class=SensorDeviceClass.HUMIDITY,
        state_class=SensorStateClass.MEASUREMENT,
        custom_unit=PERCENTAGE,
        value_fn=lambda d: _pct(_situazione(d, "@umidita")),
    ),
    IlMeteoSensorDescription(
        key="pressione",
        name="Pressione",
        device_class=SensorDeviceClass.PRESSURE,
        state_class=SensorStateClass.MEASUREMENT,
        custom_unit=UnitOfPressure.HPA,
        value_fn=lambda d: _pressure(_situazione(d, "@pressione")),
    ),
    IlMeteoSensorDescription(
        key="vento",
        name="Velocità Vento",
        device_class=SensorDeviceClass.WIND_SPEED,
        state_class=SensorStateClass.MEASUREMENT,
        custom_unit=UnitOfSpeed.KILOMETERS_PER_HOUR,
        value_fn=lambda d: _wind_speed(_situazione(d, "@wind")),
    ),
    IlMeteoSensorDescription(
        key="condizione",
        name="Condizione Meteo",
        custom_icon="mdi:weather-partly-cloudy",
        value_fn=_descrizione,
    ),
    IlMeteoSensorDescription(
        key="ultimo_aggiornamento",
        name="Ultimo Aggiornamento",
        custom_icon="mdi:clock-outline",
        value_fn=_last_update,
    ),
    IlMeteoSensorDescription(
        key="quota_zero",
        name="Quota Zero Termico",
        state_class=SensorStateClass.MEASUREMENT,
        custom_unit="m",
        custom_icon="mdi:thermometer-lines",
        value_fn=_quota_zero,
    ),

    # ---- Riepilogo di oggi ----
    IlMeteoSensorDescription(
        key="max_oggi",
        name="Temperatura Massima Oggi",
        device_class=SensorDeviceClass.TEMPERATURE,
        custom_unit=UnitOfTemperature.CELSIUS,
        value_fn=lambda d: _temp(_oggi(d).get("@max")),
    ),
    IlMeteoSensorDescription(
        key="min_oggi",
        name="Temperatura Minima Oggi",
        device_class=SensorDeviceClass.TEMPERATURE,
        custom_unit=UnitOfTemperature.CELSIUS,
        value_fn=lambda d: _temp(_oggi(d).get("@min")),
    ),
    IlMeteoSensorDescription(
        key="aria_iqa",
        name="Qualità dell'Aria (IQA)",
        custom_icon="mdi:air-filter",
        value_fn=lambda d: _oggi(d).get("@aria_iqa"),
    ),
    IlMeteoSensorDescription(
        key="aria_pollini",
        name="Livello Pollini",
        custom_icon="mdi:flower-pollen",
        value_fn=lambda d: _oggi(d).get("@aria_pollini"),
    ),
    IlMeteoSensorDescription(
        key="precipitazioni_oggi",
        name="Precipitazioni Oggi",
        custom_icon="mdi:weather-rainy",
        value_fn=lambda d: _oggi(d).get("@precipitazioni_valore"),
    ),
    IlMeteoSensorDescription(
        key="attendibilita",
        name="Attendibilità Previsione",
        state_class=SensorStateClass.MEASUREMENT,
        custom_unit=PERCENTAGE,
        custom_icon="mdi:chart-line",
        value_fn=lambda d: _float(_oggi(d).get("@attendibilita_prob")),
    ),

    # ---- Riepilogo di domani ----
    # Nota: ilMeteo non fornisce un testo descrittivo per i giorni futuri,
    # solo il simbolo numerico. Qui esponiamo la condizione HA corrispondente
    # (es. "partlycloudy") invece del testo italiano usato per "oggi".
    IlMeteoSensorDescription(
        key="condizione_domani",
        name="Condizione Meteo Domani",
        custom_icon="mdi:weather-partly-cloudy",
        value_fn=lambda d: _condition_from_simbolo(_domani(d).get("@simbolo", "")),
    ),
    IlMeteoSensorDescription(
        key="max_domani",
        name="Temperatura Massima Domani",
        device_class=SensorDeviceClass.TEMPERATURE,
        custom_unit=UnitOfTemperature.CELSIUS,
        value_fn=lambda d: _temp(_domani(d).get("@max")),
    ),
    IlMeteoSensorDescription(
        key="min_domani",
        name="Temperatura Minima Domani",
        device_class=SensorDeviceClass.TEMPERATURE,
        custom_unit=UnitOfTemperature.CELSIUS,
        value_fn=lambda d: _temp(_domani(d).get("@min")),
    ),
    IlMeteoSensorDescription(
        key="precipitazioni_domani",
        name="Precipitazioni Domani",
        custom_icon="mdi:weather-rainy",
        value_fn=lambda d: _precip_mm(_domani(d).get("@precipitazioni_valore")),
    ),
    IlMeteoSensorDescription(
        key="attendibilita_domani",
        name="Attendibilità Previsione Domani",
        state_class=SensorStateClass.MEASUREMENT,
        custom_unit=PERCENTAGE,
        custom_icon="mdi:chart-line",
        value_fn=lambda d: _float(_domani(d).get("@attendibilita_prob")),
    ),
    IlMeteoSensorDescription(
        key="aria_iqa_domani",
        name="Qualità dell'Aria (IQA) Domani",
        custom_icon="mdi:air-filter",
        value_fn=lambda d: _domani(d).get("@aria_iqa"),
    ),
    IlMeteoSensorDescription(
        key="aria_pollini_domani",
        name="Livello Pollini Domani",
        custom_icon="mdi:flower-pollen",
        value_fn=lambda d: _domani(d).get("@aria_pollini"),
    ),
]


# ---------- setup ----------

async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([
        IlMeteoSensor(coordinator, entry, desc) for desc in SENSORS
    ])


# ---------- entity ----------

class IlMeteoSensor(CoordinatorEntity, SensorEntity):
    """Sensore generico ilMeteo."""

    def __init__(self, coordinator, entry: ConfigEntry, desc: IlMeteoSensorDescription) -> None:
        super().__init__(coordinator)
        self._desc = desc
        self._attr_unique_id = f"ilmeteo_{entry.data['location_id']}_{desc.key}"
        self._attr_name = f"{entry.data.get('name', 'ilMeteo')} {desc.name}"
        if desc.custom_unit:
            self._attr_native_unit_of_measurement = desc.custom_unit
        if desc.device_class:
            self._attr_device_class = desc.device_class
        if desc.state_class:
            self._attr_state_class = desc.state_class
        if desc.custom_icon:
            self._attr_icon = desc.custom_icon

    @property
    def native_value(self) -> Any:
        if self.coordinator.data and self._desc.value_fn:
            return self._desc.value_fn(self.coordinator.data)
        return None
