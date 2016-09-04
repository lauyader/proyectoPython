#!/usr/bin/python
# -*- coding: utf-8 -*-
import mysql.connector


code =raw_input("Cedula:")
name=raw_input("Nombre:")
email=raw_input("Email:")

# Variable con la configuracion de la conexion
config_mysql = {
    'user': 'root',
    'password': 'weEAr9o63',
    'host': 'localhost',
    'database': 'Evaluacion',
}

# conectamos al servidor MySql
conexion_mysql = mysql.connector.connect(**config_mysql)


print code



cursor = conexion_mysql.cursor()
sql = "INSERT INTO Datos(cedula, ape_nom, email) VALUES('%s','%s','%s')"%(code,name,email)
cursor.execute(sql)


#guardamos cambios en la base de datos
conexion_mysql.commit()



# Cerramos la conexión
cursor.close()

print "Proceso concluido"
