#!/usr/bin/python
# -*- coding: utf-8 -*-

# ##########################################################
# Programa de consulta mysql y python
# ##########################################################

import mysql.connector


code = raw_input("Cedula:")


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
sql = "SELECT cedula, ape_nom FROM Datos WHERE cedula='%s'" %code
#sql = "SELECT cedula, ape_nom FROM Datos WHERE cedula=7089271"
cursor.execute(sql)
'''
resultado = cursor.fetchall()
for registro in resultado:
    print (registro)
'''
###########################################################
# fetchone muestra el registro
###########################################################
registro = cursor.fetchone()
cierre = 0
while (registro != None):
   print (registro)

   registro = cursor.fetchone()
   cierre = 1



if cierre == 0:
	print "Cédula no existe"
else:
	print 'Registro encontrado'
# Cerramos la conexión
cursor.close()

print "Proceso concluido"
