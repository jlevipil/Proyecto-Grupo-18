# Proyecto Grupo 18.
## Pagina Web: https://jlevipil.github.io/Proyecto-Grupo-18/
## Streaming inteligente. Eligiendo la mejor plataforma para ver películas
Este proyecto busca identificar cuál plataforma de streaming ofrece la mejor relación entre calidad y precio, considerando tanto el costo mensual como la amplitud, diversidad y calidad del catálogo disponible. La motivación surge del crecimiento acelerado del mercado del streaming, donde muchos usuarios mantienen más de una suscripción sin evaluar si realmente están obteniendo un valor adecuado por su gasto. Dado que gran parte del contenido se repite entre servicios y que la oferta total puede ser difícil de comparar, este análisis pretende entregar una visión clara y basada en datos para facilitar una decisión informada.

Para ello, se recopilaron datos desde Watchmode API y los IMDb Non-Commercial Datasets, integrando información sobre títulos, géneros, años de estreno, ratings, directores, actores y disponibilidad en distintas plataformas.

Este proyecto está dirigido a usuarios de servicios de streaming, familias y personas que buscan optimizar sus gastos, así como a quienes desean comprender mejor cómo varía la oferta de contenido entre plataformas. En conjunto, el trabajo entrega una herramienta práctica y basada en evidencia para elegir la plataforma que mejor se ajuste a las necesidades y preferencias de cada usuario.

## Estructura del Repositorio
```bash
📦 Proyecto-Grupo-18
│
├── 📂 data: Contiene los datos extraídos tanto crudos como limpios
│
├── 📂 imbd_plataformas: Contiene notebooks en el que se crean y limpian los csv de IMDB
│   └── 📄 imdb_<plataforma>.ipynb
│
├── 📂 img: Contiene imágenes de los gráficos y demás cosas utilizadas en el análisis
│
├── 📂 limpiezas_plataformas: Contiene notebooks en el que se piden y limpian los datos de la API
│   └── 📄 limpieza_<plataforma>.ipynb
│
├── 📂 pdf: Contiene PDF sobre el proyecto
│   ├── Propuesta Proyecto(...).pdf
│   └── Proyecto.pdf
│
├── 📂 src: Contiene funciones y constantes útiles para la extracción de datos
│   ├── buscar_peliculas.py: Contiene la función para pedir datos a la API
│   ├── constantes.py: Contiene las constantes utilizadas en la función
│   └── apikey.txt: Como la APIKEY es propia no se sube, pero deberia estar en esta carpeta
│
├── 📄 Repositorio Final.ipynb
│
└── 📄 Repositorio Inicial.ipynb
```

## Integrantes
- Andrea Riquelme: Líder de Grupo
- Adrian Huizi: Análisis de Datos
- Catalina Díaz: Análisis de Datos
- Juan Levipil: Extracción de Datos

## Librerías Usadas
- `requests`
- `numpy`
- `pandas`
- `matplotlib`
- `seaborn `
- `sklearn`
- `ast`

## Guia de Ejecución
Para actualizar los datos y hacer el análisis denuevo siga esta guía
### Archivos Extra Necesarios
- Colocar el archivo `apikey.txt` en la carpeta `src/`. Este archivo debe contener la API key conseguida en la pagina de Watchmode. `https://api.watchmode.com/requestApiKey`
- Colocar los archivos `.tsv` en la carpeta `data/`. Estos se consiguen en la pagina de IMDB `https://developer.imdb.com/non-commercial-datasets/`
### Obtención de Datos
- Seguir las instruciones y ejecutar las celdas de los archivos `limpieza_<plataforma>.ipynb` de la carpeta `limpiezas_plataformas/` para conseguir los datos de la API de Watchmode. Se generaran los archivos `.csv`.
- Seguir las instrucciones y ejecutar las celdas de los archivos `imdb_<plataforma>.ipynb` de la carpeta `imbd_plataformas/` para conseguir los datos de IMBD y juntarlos con los de Watchmode. Se generaran los archivos `.csv`
### Análisis de los Datos
- Seguir las instrucciones y ejecutar las celdas del archivo `Repositorio Inicial.ipynb`
