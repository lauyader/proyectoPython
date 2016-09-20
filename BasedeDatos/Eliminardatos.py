#!/usr/bin/python
# -*- coding: utf-8 -*-
import mysql.connector


code =raw_input("Cedula:")


# Variable con la configuracion de la conexion
config_mysql = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'Evaluacion',
}

# conectamos al servidor MySql
conexion_mysql = mysql.connector.connect(**config_mysql)






cursor = conexion_mysql.cursor()
sql = "SELECT cedula, ape_nom, email FROM Datos WHERE cedula='%s'"%code
#sql = "SELECT cedula, ape_nom FROM Datos WHERE cedula=7089271"
cursor.execute(sql)

'''
resultado = cursor.fetchall()
for registro in resultado:
    print (registro)

'''
registro = cursor.fetchone()
while (registro != None):
   print (registro)

   registro = cursor.fetchone()

#guardamos cambios en la base de datos
#conexion_mysql.commit()



# Cerramos la conexión
cursor.close()

print "Proceso concluido"
