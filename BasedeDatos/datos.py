#!/usr/bin/python
# -*- coding: utf-8 -*-
import mysql.connector

# Variable con la configuracion de la conexion
config_mysql = {
    'user': 'root',
    'password': 'weEAr9o63',
    'host': 'localhost',
    'database': 'Evaluacion',
}

# conectamos al servidor MySql
conexion_mysql = mysql.connector.connect(**config_mysql)



cursor = conexion_mysql.cursor()

cursor.execute("SELECT cedula, ape_nom, email FROM Datos")

for (cedula, ape_nom, email) in cursor:
    print("Cedula: " + cedula + ", Apellido y Nombre: " + ape_nom + ", Email: " + email)

# Cerramos la variable encargada de las consultas
cursor.close()


# Cerramos la conexión
conexion_mysql.close()    