import mysql.connector
from tabulate import tabulate

# Datos de conexión
usuario = "root"  
contrasena = "1234"  
base_datos = "CochesDB"  
host = "172.17.0.4"  # IP del contenedor Docker
puerto = 3306  # Puerto de MySQL

# Conexión a MySQL
conexion = mysql.connector.connect(
    host=host,
    user=usuario,
    password=contrasena,
    database=base_datos,
    port=puerto
)

cursor = conexion.cursor()

# Obtener datos de la tabla
cursor.execute("SELECT id, marca, modelo, color, km, precio FROM Coches")
datos = cursor.fetchall()

# Encabezados de la tabla
encabezados = ["ID", "MARCA", "MODELO", "COLOR", "KM", "PRECIO"]

# Imprimir tabla
print(tabulate(datos, headers=encabezados, tablefmt="grid"))

# Cerrar conexión
cursor.close()
conexion.close()