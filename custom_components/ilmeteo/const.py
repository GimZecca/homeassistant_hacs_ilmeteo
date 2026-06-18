"""Costanti per l'integrazione ilMeteo."""

DOMAIN = "ilmeteo"

# Endpoint API
BASE_URL = "https://iphone.ilmeteo.it/ajax_app.php"
WS_VERSION = "5.3"

# Chiave usata dall'app ufficiale per il calcolo del token giornaliero.
# Ottenuta tramite reverse engineering dell'APK Android (classe MeteoDataParse).
# Formula: x = MD5(method + WS_X_KEY + dayOfMonth)
WS_X_KEY = "-mobileApp-"

# Update interval in minuti
UPDATE_INTERVAL_MINUTES = 10

# Storage
STORAGE_KEY_COMUNI = "ilmeteo_comuni"
STORAGE_VERSION = 1
