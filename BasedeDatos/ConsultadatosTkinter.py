#!/usr/bin/python
# -*- coding: utf-8 -*-
# www.pythondiario.com

import sys
from Tkinter import *
import mysql.connector



# Variable con la configuracion de la conexion
config_mysql = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'Evaluacion',
}

# conectamos al servidor MySql
conexion_mysql = mysql.connector.connect(**config_mysql)

#ced = ci.get()


def hacer_click():
    """
	try:
		# _valor = int(entrada_texto.get())
		cursor = conexion_mysql.cursor()
		sql = "SELECT cedula, ape_nom FROM Datos WHERE cedula='%s'" %valor

 
		cursor.execute(sql)
		###########################################################
		# fetchone muestra el registro
		###########################################################
		registro = cursor.fetchone()
		print valor 
		cierre = 0
		while (registro != None):
		   print (registro)

		   registro = cursor.fetchone()
		   cierre = 1
		   entrada_texto = Entry(vp, width=10, textvariable=valor)
		   entrada_texto.grid(column=2, row=1)


		if cierre == 0:
			print "Cédula no existe"
		else:
			print 'Registro encontrado'
            #mensaje = 'Registro no encontrado'
		   
		#registro2 = str(registro.get())

		etiqueta.config(entrada_text = registro)
        except ValueError:
        	etiqueta.config(text="Introduce un numero!")
    """
def clic():
    
        valor = int(entrada_texto.get())
        print valor
        etiqueta.config(text = valor)
        cursor = conexion_mysql.cursor()
        sql = "SELECT cedula, ape_nom, email FROM Datos WHERE cedula='%s'" %valor
        cursor.execute(sql)
        registro = cursor.fetchone()
        while (registro != None):
            #entiqueta.config(text = valor)
            ###########################################################
            # Fragmento el vector del registro
            ###########################################################
            
            etiqueta.config(text=registro[0])
            Cnombre.config(text=registro[1])
            Cemail.config(text=registro[2])
            cursor.close() 
            return
        else:
            valor="no existe" 
            etiqueta.config(text=valor)
            entrada_texto.config(texto="")
            print valor
            return



app = Tk()
app.geometry("640x480+0+0")
app.title("Consulta por Cédula")


#u = tkinter.StringVar()
#Ventana Principal
vp = Frame(app)
vp.grid(column=0, row=0, padx=(50,50), pady=(10,10))
vp.columnconfigure(0, weight=1)
vp.rowconfigure(0, weight=1)

###########################################################
# Pedir los datos a consultar
###########################################################

cedula = Label(vp, text="Introduce el Número de Cédula:", font=("Helvetica", 12, 'bold'))
cedula.grid(column=1, row=3)

boton = Button(vp, text="Buscar", command=clic)
boton.grid(column=3, row=3)

valor = ""
entrada_texto = Entry(vp, width=10, textvariable=valor)
entrada_texto.grid(column=2, row=3)

etiqueta = Label(vp, text="Valor")
etiqueta.grid(column=2, row=4, sticky=(W,E))

###########################################################
# Mostrar los resultados de la  consulta
###########################################################
Ccedula =Label(vp, text="Cedula de Identidad:",  font=("Helvetica", 12, 'bold'), anchor=E, justify=LEFT)
Ccedula.grid(column=1, row=4, sticky=(W,E))
etiqueta = Label(vp, text="?", font=("Helvetica", 12), anchor=W, justify=LEFT)
etiqueta.grid(column=2, row=4, sticky=(W,E))

Enombre = Label(vp, text="Apellido y Nombre:", font=("Helvetica", 12, 'bold'), anchor=E, justify=LEFT)
Enombre.grid(column=1, row=5, sticky=(W,E))

Cnombre = Label(vp, text="?", font=("Helvetica", 12), anchor=W, justify=LEFT)
Cnombre.grid(column=2, row=5, sticky=(W,E))


Eemail = Label(vp, text="Email:", font=("Helvetica", 12, 'bold'), anchor=E, justify=LEFT)
Eemail.grid(column=1, row=6, sticky=(W,E))

Cemail = Label(vp, text="?", font=("Helvetica", 12), anchor=W, justify=LEFT)
Cemail.grid(column=2, row=6, sticky=(W,E))

###########################################################
# Boton de salir de la aplicacioón de consulta
###########################################################
Salir = Button(vp, text='Salir', command=vp.destroy)
Salir.grid(column=2, row=12)
app.mainloop()
