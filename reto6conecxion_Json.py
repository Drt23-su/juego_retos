import mysql.connector
import json
from tabulate import tabulate

# Leer datos de conexión desde un archivo JSON
with open("config.json", "r") as config_file:
    config = json.load(config_file)

# Conexión a MySQL
conexion = mysql.connector.connect(
    host=config["host"],
    user=config["usuario"],
    password=config["contraseña"],
    database=config["base_datos"],
    port=config["puerto"]
)

cursor = conexion.cursor()

# Obtener datos de la tabla
cursor.execute("SELECT id, marca, modelo, color, km, precio FROM Coches")
datos = cursor.fetchall()

# Encabezados de la tabla
encabezados = ["ID", "MARCA", "MODELO", "COLOR", "KM", "PRECIO"]

# Imprimir tabla
print(tabulate(datos, headers=encabezados, tablefmt="grid"))

# Cerrar conexion
cursor.close()
conexion.close()
