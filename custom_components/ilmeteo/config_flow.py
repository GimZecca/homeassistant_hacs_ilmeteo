"""Config flow per ilMeteo con ricerca comune per nome (da API getDB)."""
from __future__ import annotations

import logging

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.exceptions import HomeAssistantError
from homeassistant.helpers.selector import (
    SelectSelector,
    SelectSelectorConfig,
    SelectSelectorMode,
    TextSelector,
    TextSelectorConfig,
    TextSelectorType,
)

from . import DOMAIN, async_fetch_data
from .comuni_api import async_get_comuni, search_comuni

_LOGGER = logging.getLogger(__name__)

DOC_URL = "https://www.ilmeteo.it/portale/files/ilmeteo_doc_xml_codici_comuni.pdf"


class IlMeteoConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Config flow a tre passi: cerca → seleziona → conferma."""

    VERSION = 1

    def __init__(self):
        self._comuni: dict = {}
        self._search_results: list[dict] = []

    async def async_step_user(self, user_input=None):
        """Passo 1: campo di ricerca per nome comune."""
        errors = {}

        if not self._comuni:
            self._comuni = await async_get_comuni(self.hass)

        if user_input is not None:
            query = user_input.get("search", "").strip()
            if len(query) < 2:
                errors["search"] = "too_short"
            else:
                self._search_results = search_comuni(self._comuni, query)
                if not self._search_results:
                    errors["search"] = "no_results"
                else:
                    return await self.async_step_select()

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("search"): TextSelector(
                    TextSelectorConfig(type=TextSelectorType.TEXT)
                ),
            }),
            errors=errors,
            description_placeholders={
                "example": "es. Milano, Roma, Torino...",
            },
        )

    async def async_step_select(self, user_input=None):
        """Passo 2: lista dropdown con i risultati della ricerca."""
        errors = {}

        if user_input is not None:
            chosen_label = user_input.get("location", "")

            if chosen_label == "__manual__":
                return await self.async_step_manual()

            chosen = next(
                (r for r in self._search_results if r["label"] == chosen_label),
                None,
            )
            if not chosen:
                errors["location"] = "invalid_selection"
            else:
                location_id = int(chosen["id"])
                try:
                    nome = await self._validate(location_id)
                    return self.async_create_entry(
                        title=nome,
                        data={"location_id": location_id, "name": nome},
                    )
                except CannotConnect:
                    errors["location"] = "cannot_connect"

        return self.async_show_form(
            step_id="select",
            data_schema=vol.Schema({
                vol.Required("location"): SelectSelector(
                    SelectSelectorConfig(
                        options=[
                            {"value": r["label"], "label": r["label"]}
                            for r in self._search_results
                        ] + [{"value": "__manual__", "label": "✏️ Inserisci ID manualmente..."}],
                        mode=SelectSelectorMode.LIST,
                    )
                ),
            }),
            errors=errors,
            description_placeholders={
                "count": str(len(self._search_results)),
                "doc_url": DOC_URL,
            },
        )

    async def async_step_manual(self, user_input=None):
        """Passo alternativo: inserisci l'ID numerico direttamente."""
        errors = {}

        if user_input is not None:
            try:
                location_id = int(user_input["location_id"])
                nome = await self._validate(location_id)
                return self.async_create_entry(
                    title=nome,
                    data={"location_id": location_id, "name": nome},
                )
            except (ValueError, TypeError):
                errors["location_id"] = "invalid_id"
            except CannotConnect:
                errors["location_id"] = "cannot_connect"

        return self.async_show_form(
            step_id="manual",
            data_schema=vol.Schema({
                vol.Required("location_id"): TextSelector(
                    TextSelectorConfig(type=TextSelectorType.NUMBER)
                ),
            }),
            errors=errors,
            description_placeholders={
                "doc_url": DOC_URL,
            },
        )

    async def _validate(self, location_id: int) -> str:
        """Verifica l'ID e restituisce il nome della città dall'API."""
        try:
            data = await async_fetch_data(self.hass, location_id)
            nome = data.get("localita", {}).get("@nome", "")
            return nome or f"Località {location_id}"
        except Exception as err:
            raise CannotConnect(str(err)) from err


class CannotConnect(HomeAssistantError):
    """Errore di connessione."""
