# ilMeteo.it — Home Assistant Integration

[![HACS Custom](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/hacs/integration)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Integrazione non ufficiale per [ilMeteo.it](https://www.ilmeteo.it) che porta le previsioni meteo italiane in Home Assistant.

> **Disclaimer:** This integration is unofficial and not affiliated with ilMeteo.it.
> It uses an undocumented API discovered through reverse engineering of the official
> Android app, intended for personal, non-commercial use only. Use at your own risk.

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

Il database comuni (~8000 località) viene scaricato automaticamente dall'API
ilMeteo al primo avvio e cachato localmente. Non è necessario conoscere l'ID
numerico — la ricerca per nome funziona immediatamente.

### Trovare l'ID manualmente (opzionale)

Se la ricerca non trova il tuo comune, puoi inserire l'ID numerico direttamente.
Esempi comuni:

| Città | ID |
|---|---|
| Roma | 11 (Accadia)… cerca su ilmeteo.it |
| Milano | 149 |
| Arco (TN) | 300 |

Il modo più affidabile è intercettare il traffico dell'app ufficiale o cercare
il numero nel codice sorgente HTML di [ilmeteo.it](https://www.ilmeteo.it).

---

## Aggiornamento dati

Le previsioni si aggiornano ogni **10 minuti**, in linea con l'app ufficiale.

---

## Note tecniche

### Token di autenticazione

L'API richiede un parametro `x` calcolato giornalmente:

```
x = MD5(method + "-mobileApp-" + dayOfMonth)
```

Questa formula è stata ricavata dall'analisi della classe `MeteoDataParse`
dell'APK Android ufficiale con [jadx](https://github.com/skylot/jadx).

### Database comuni

I comuni vengono scaricati dall'endpoint `getDB` dell'API ilMeteo, che restituisce
un CSV semicolon-separated con ID, provincia, regione, nome, coordinate e altitudine.
Il database viene cachato nello storage di Home Assistant per evitare download
ripetuti ad ogni riavvio.

---

## Contribuire

Pull request benvenute. Per segnalare problemi apri una issue su GitHub.

## Licenza

MIT — vedi [LICENSE](LICENSE).
