#!/usr/bin/python

import sys
from Tkinter import *


raiz = Tk()
raiz.title("Mi primera aplicacion")
#'''barraMenu = ("ventana")'''

etiqueta = Label(raiz, text="Hola mundo")
boton = Button(raiz, text="Clic")


etiqueta.pack()
boton.pack()

raiz.mainloop()