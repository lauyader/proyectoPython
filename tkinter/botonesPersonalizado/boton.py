#!/usr/bin/python
# -*- coding: utf-8 -*-


###########################################################
#Importar librerias de ventanas
###########################################################
from Tkinter import *
State = False

###########################################################
#Declaracion de las funciones
###########################################################
def Change(event):
	global State 
	if State == True:
		lbl.config(image = btnFalse)
		print 'Opcion Falsa'
		State = False
	else:
		lbl.config(image = btnTrue)
		print 'Opcion Verdadera'
		State = True 




###########################################################
#Pasar Tkinter a una variable
###########################################################
ventana = Tk()

###########################################################
#Dimension de la ventana
###########################################################
ventana.geometry("640x480+0+0")
ventana.config(bg="white")
ventana.title("Boton Personalizado")

###########################################################
# Asignar los archivos imagen a las variables
###########################################################
btnFalse = PhotoImage(file = 'btnOff.png')
btnTrue = PhotoImage(file = 'btnOn.png')

###########################################################
#Asignación de las Etiquetas a las imagenes del boton
###########################################################

lbl = Label(ventana,image = btnFalse)
lbl.bind('<Button-1>', Change)
lbl.place(x=20,y=50)


ventana.mainloop()
