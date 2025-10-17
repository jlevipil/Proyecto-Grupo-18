import requests as rq
import pandas as pd
from src.constantes import API_KEY, URL_BASE, PLATAFORMAS, REGION

def buscar_peliculas(plataforma):
    ## Parametros del GET
    parametros = {
        'apiKey': API_KEY,
        'types': 'movie',
        # 'regions': REGION,  # Por alguna razon la request no funciona al especificar la region asi que queda comentada
        'source_ids': PLATAFORMAS[plataforma]
    }
    url_get = URL_BASE + 'list-titles/'

    ## Primer get
    response = rq.get(url_get, params=parametros)
    json_1 = response.json()
    
    print(response, json_1['total_pages'], json_1['total_results'])
    
    paginas_totales = json_1['total_pages']
    df_1 = pd.DataFrame(json_1['titles'])
    resultados_totales = json_1['total_results']

    # Ciclo
    dataframes = [df_1]

    for i in range(2, paginas_totales + 1):
        parametros['page'] = i
        response = rq.get(url_get, params=parametros)
        json_n = response.json()
        df_n = pd.DataFrame(json_n['titles'])
        dataframes.append(df_n)

    # Se juntan todos los DataFrames
    dataframe_final = pd.concat(dataframes, ignore_index=True)
    return (dataframe_final, resultados_totales)