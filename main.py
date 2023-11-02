import math
import pyproj
import csv
import os

# Definir las proyecciones
utm_zone = pyproj.CRS("epsg:25830")

def clear_terminal():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')

def latlon_to_utm(lat, lon):
    transformer = pyproj.Transformer.from_crs("epsg:4326", utm_zone, always_xy=True)
    x, y = transformer.transform(lon, lat)
    return x, y

def utm_to_latlon(x, y):
    transformer = pyproj.Transformer.from_crs(utm_zone, "epsg:4326", always_xy=True)
    lon, lat = transformer.transform(x, y)
    return lat, lon

def direct_problem(lat1, lon1, distance, azimuth):
    x1, y1 = latlon_to_utm(lat1, lon1)

    # Convertir el acimut a radianes
    azimuth = math.radians(azimuth)

    # Calcular la nueva posición UTM
    x2 = x1 + (distance * math.cos(azimuth))
    y2 = y1 + (distance * math.sin(azimuth))

    # Convertir la nueva posición UTM a latitud y longitud
    lat2, lon2 = utm_to_latlon(x2, y2)

    return lat2, lon2

def inverse_problem(lat1, lon1, lat2, lon2):
    x1, y1 = latlon_to_utm(lat1, lon1)
    x2, y2 = latlon_to_utm(lat2, lon2)

    # Calcular la diferencia en las coordenadas UTM
    dx = x2 - x1
    dy = y2 - y1

    # Calcular la distancia en UTM
    distance = math.sqrt(dx**2 + dy**2)

    # Calcular el acimut
    azimuth = math.degrees(math.atan2(dy, dx))

    return distance, azimuth

def get_input_from_csv(csv_file):
    data = []
    with open(csv_file, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=';')  # Utiliza el separador de columna correcto
        next(csvreader, None)  # Omitir la primera fila (encabezado)
        for row in csvreader:
            if len(row) == 5:
                # Verificar que los valores no estén vacíos antes de convertirlos
                if all(row):
                    lat, lon, distance, azimuth, name = map(float, row)
                    data.append((lat, lon, distance, azimuth, name))
    return data

# Llama a la función para borrar la terminal
clear_terminal()

# Ejemplo de uso
print("Seleccione una opción:")
print("1. Entrada por teclado")
print("2. Cargar datos desde un archivo CSV")
option = int(input("Opción (1/2): "))

if option == 1:
    lat1 = float(input("Latitud inicial (en grados): "))
    lon1 = float(input("Longitud inicial (en grados): "))
    distance = float(input("Distancia (en metros): "))  # Cambiar a metros
    azimuth = float(input("Acimut (en grados): "))
    
    lat2, lon2 = direct_problem(lat1, lon1, distance, azimuth)
    print(f"Coordenada final en UTM: X={lat2}, Y={lon2}")
    
elif option == 2:
    print("Recuerda que el .csv debe tener las columnas en el siguiente orden: (latitud;longitud;acimut;distancia;nombre) separado por punto y coma y con punto como separador decimal")
    csv_file = input("Introduce el nombre del archivo CSV (ejemplo.csv): ")
    data = get_input_from_csv(csv_file)
    results = []

    for lat1, lon1, azimuth, distance, name in data:
        lat2, lon2 = direct_problem(lat1, lon1, distance, azimuth)
        results.append((lat2, lon2, distance, azimuth, name))

    output_file = input("Nombre del archivo CSV de salida (resultados.csv): ")
    with open(output_file, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=';')  # Utiliza el separador de columna correcto
        csvwriter.writerow(["Latitud", "Longitud", "Acimut", "Distancia", "Nombre"])
        for result in results:
            csvwriter.writerow(result)
    print(f"Resultados guardados en {output_file}")

else:
    print("Opción no válida. Debe elegir 1 o 2.")
