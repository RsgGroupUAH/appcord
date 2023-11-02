# Requerimientos

## Librerías
numpy==1.19.5
pandas==1.2.4
matplotlib==3.4.2
scikit-learn==0.24.2

## Formato de datos
Los datos de entrada deben estar en formato CSV (filas separadas por comas y separador decimal el punto), con las siguientes columnas:
- Sin encabezado
- `xGeo`: Coordenada Latitud del punto.
- `yGeo`: Coordenada Longitud del punto.
- `m`: Orientación en grados del punto.
- `azh`: Distancia en m.
- `iD`: Identificador del punto.  