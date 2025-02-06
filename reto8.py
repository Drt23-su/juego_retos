from pymongo import MongoClient
from prettytable import PrettyTable

# Datos de conexión
usuario = "root"  
contrasena = "1234"  
base_datos = "concesionario"  

# Construcción de la URI para conexión
uri = f"mongodb://{usuario}:{contrasena}@172.17.0.3:27017/{base_datos}?authSource=admin"

# Conexión a MongoDB
cliente = MongoClient(uri)

# Verificar que la base de datos existe
print("Bases de datos disponibles:", cliente.list_database_names())

db = cliente["concesionario"]
coleccion = db["coche"]

# Convertir el cursor a lista para poder reutilizarlo
coches = list(coleccion.find())


# Crear la tabla con PrettyTable
tabla = PrettyTable(["_id", "ID", "Marca", "Modelo", "Color", "Kilometraje", "Precio"])

# Poblar la tabla
for coche in coches:
    tabla.add_row([
        coche.get("_id", ""),  # Obtener el ID de MongoDB
        coche.get("id", ""),  # Aquí debe ser "id" en minúscula, ya que en los documentos de Mongo aparece así
        coche.get("marca", ""),
        coche.get("modelo", ""),
        coche.get("color", ""),
        coche.get("km", ""),
        coche.get("precio", "")
    ])

# Imprimir la tabla
print(tabla)

