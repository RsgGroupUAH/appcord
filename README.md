# Aplicación de Cálculo de Coordenadas en Python 3.8.5
Esta aplicación desarrollada en Python 3 permite a los usuarios realizar cálculos geoespaciales precisos al calcular las coordenadas de un punto a partir de un punto de origen, una distancia y un acimut, o viceversa, calcular la distancia y el acimut entre dos puntos geográficos dados. La aplicación se presenta como una interfaz de línea de comandos (CLI) que ofrece al usuario dos opciones principales al iniciar: el cálculo mediante la entrada de un CSV y valor por valor.

La función direct_problem, que es la funcionalidad que está implementada en esta versión, realiza el cálculo del problema directo en el contexto de coordenadas geográficas y UTM (Universal Transverse Mercator). Este cálculo se utiliza para encontrar las coordenadas geográficas (latitud y longitud) de un punto (lat2, lon2) dado un punto de inicio (lat1, lon1), una distancia y un acimut.

A continuación, descompondremos esta función paso a paso:

- x1, y1 = latlon_to_utm(lat1, lon1): Esta línea llama a la función latlon_to_utm para convertir las coordenadas geográficas iniciales (lat1, lon1) en coordenadas UTM. La función latlon_to_utm utiliza una proyección para realizar esta conversión.

- azimuth = math.radians(azimuth): Aquí, el acimut dado en grados se convierte a radianes. El acimut es la dirección del punto final con respecto al punto de inicio.

- x2 = x1 + (distance * math.cos(azimuth)): Utilizando la fórmula de trigonometría, se calcula la nueva posición UTM en la dirección este-oeste (X) a partir de la posición inicial (x1). La fórmula implica que se suma la distancia deseada multiplicada por el coseno del acimut al valor X inicial.

- y2 = y1 + (distance * math.sin(azimuth)): De manera similar, se calcula la nueva posición UTM en la dirección norte-sur (Y) a partir de la posición inicial (y1). La fórmula involucra sumar la distancia deseada multiplicada por el seno del acimut al valor Y inicial.

- lat2, lon2 = utm_to_latlon(x2, y2): Por último, la función convierte las coordenadas UTM calculadas (x2, y2) en coordenadas geográficas (latitud y longitud) utilizando la función utm_to_latlon.

En resumen, esta función toma las coordenadas geográficas iniciales (lat1, lon1), una distancia y un acimut, y calcula las coordenadas geográficas del punto final (lat2, lon2) utilizando proyecciones y cálculos trigonométricos.

A continuación, se presenta una descripción más detallada de estas dos funcionalidades:

## Funcionalidades
### Funcionalidad 1: Entrada csv
Esta opción permite a los usuarios cargar datos desde un archivo CSV. El archivo CSV debe seguir un formato específico con las columnas en el orden de latitud, longitud, acimut, distancia y nombre. Los valores en el archivo CSV deben estar separados por punto y coma (;) y con el punto como separador decimal. La aplicación procesa los datos del archivo CSV y realiza el cálculo del problema directo para encontrar la coordenada final en el sistema UTM, que incluye las coordenadas UTM (X e Y), distancia y acimut. Luego, se guarda el resultado en otro archivo CSV con las columnas correspondientes.

### Funcionalidad 2: Cálculo valor por valor
Esta opción permite a los usuarios ingresar manualmente datos como la latitud inicial, longitud inicial, distancia en metros y acimut en grados. La aplicación realiza el cálculo del problema directo para encontrar la coordenada final en el sistema UTM, incluyendo las coordenadas UTM (X e Y). Luego, muestra los resultados en la pantalla.

La aplicación también maneja casos de error, como asegurarse de que las columnas del archivo CSV estén en el orden correcto y que los valores sean números válidos. Además, el menú es interactivo y guía al usuario a través de las dos funcionalidades disponibles.


## Referencias
1. [pyproj.Proj is functionally equivalent to the proj command line tool in PRO](https://pyproj4.github.io/pyproj/stable/api/proj.html).
2. [Problem transforming coordinates with PyProj](https://gis.stackexchange.com/questions/388531/problem-transforming-coordinates-with-pyproj).
3. [Calculadora Geodésica](https://www.ign.es/web/ign/portal/calculadora-geodesica).