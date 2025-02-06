import mysql.connector
from prettytable import PrettyTable;
#Datos de conexion:
config = {
    'user':'root','password':'1234',
    'host':'172.17.0.4','database':'CochesDB'
}
connection = mysql.connector.connect(**config)
#creo el objeto que gestionara la llamada
#y el retorno de los datos en python,cursor.
cursor = connection.cursor()
cursor.execute("select * from Coches")
#Los paso a un diccionario para leerlo con un bucle
res = cursor.fetchall()
#nos sirve para crear una tabla(variable llamada tabla)
tabla = PrettyTable(["ID", "Marca", "Modelo", "Color", "Kilometraje", "Precio"])
#for coche in res:
    #print(coche)
for fila in res:
    tabla.add_row(fila)
print(tabla)
#lo que hace es que le decimos que añada una fila por cada fila de datos