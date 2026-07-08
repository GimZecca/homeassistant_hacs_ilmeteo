# ilMeteo.it — Home Assistant Integration

[![HACS Custom](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/hacs/integration)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Integrazione non ufficiale per [ilMeteo.it](https://www.ilmeteo.it) che porta le previsioni meteo italiane in Home Assistant.

> **Disclaimer:** This is an unofficial integration, not affiliated with or endorsed by ilMeteo.it.
> Intended for personal, non-commercial use only. Use at your own risk.

---

## Funzionalità

- **Entità `weather`** con:
  - Condizioni meteo correnti (temperatura, umidità, pressione, vento)
  - **Previsioni orarie** fino a 48 ore
  - **Previsioni giornaliere** fino a 15 giorni
- **14 sensori** dedicati:

  | Sensore | Unità |
  |---|---|
  | Temperatura attuale | °C |
  | Temperatura percepita | °C |
  | Temperatura min/max oggi | °C |
  | Umidità | % |
  | Pressione | hPa |
  | Velocità vento | km/h |
  | Condizione meteo | testo |
  | Qualità dell'aria (IQA) | testo |
  | Livello pollini | testo |
  | Precipitazioni oggi | mm |
  | Attendibilità previsione | % |
  | Quota zero termico | m |
  | Ultimo aggiornamento | ora |

---

## Installazione via HACS

Clicca il pulsante per aggiungere automaticamente il repository:

[![Open your Home Assistant instance and add this repository.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=GimZecca&repository=homeassistant_hacs_ilmeteo&category=integration)

Oppure manualmente:
1. In HACS → **Integrations** → ⋮ → **Custom repositories**
2. Aggiungi l'URL di questo repo, categoria **Integration**
3. Cerca **ilMeteo** e clicca **Download**
4. Riavvia Home Assistant

## Installazione manuale

1. Copia la cartella `custom_components/ilmeteo/` in `config/custom_components/`
2. Riavvia Home Assistant

---

## Configurazione

1. **Impostazioni** → **Dispositivi e Servizi** → **Aggiungi Integrazione** → cerca **ilMeteo**
2. Digita il nome del comune (es. `Milano`, `Roma`)
3. Seleziona il comune corretto dalla lista
4. Conferma

Il database dei comuni (~8000 località) viene scaricato automaticamente al primo
avvio e cachato localmente. Non è necessario conoscere l'ID numerico — la ricerca
per nome funziona immediatamente.

### Trovare l'ID manualmente (opzionale)

Se preferisci inserire l'ID numerico direttamente, puoi consultare la
[lista ufficiale dei comuni](https://www.ilmeteo.it/portale/files/ilmeteo_doc_xml_codici_comuni.pdf)
pubblicata da ilMeteo.

| Città | ID |
|---|---|
| Milano | 149 |
| Arco (TN) | 300 |

---

## Aggiornamento dati

Le previsioni si aggiornano ogni **10 minuti**.

---

## Note legali

Questa integrazione è destinata esclusivamente all'uso personale e non commerciale.
Non è affiliata né approvata da ilMeteo.it. Utilizza a tuo rischio e pericolo.

---

## Contribuire

Pull request benvenute. Per segnalare problemi apri una issue su GitHub.

## Licenza

MIT — vedi [LICENSE](LICENSE).
