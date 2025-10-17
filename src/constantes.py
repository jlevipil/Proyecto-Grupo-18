# URL base de la API
URL_BASE = 'https://api.watchmode.com/v1/'

# Leer la API key desde un archivo externo
with open('src/apikey.txt') as f:
    API_KEY = f.read().strip()   # strip() elimina espacios o saltos de línea

# Región
REGION = 'CL'

# Plataformas con su ID en Watchmode
PLATAFORMAS = {
    'Netflix': 203,
    'Hulu': 157,
    'Max': 387,
    'Prime': 26,
    'Disney+': 372,
    'Paramount+': 444
}