# -*- coding: utf-8 -*-
import modulo_db.p01 as mod
import tkinter
import tkinter.messagebox # mensajes de diálogo

def obtener_valores():
    # Obtiene los valores de los Entry's y los pasa a la función
    # que interactúa con la base de datos
 usuario = u.get()
 clave = p.get()

 val = mod.validar_usuario(usuario, clave)
    # Si el valor retornado es 1 significa que la consulta tuvo éxito
 if val > 0:
  tkinter.messagebox.showinfo("mensaje", "Bienvenido %s"%(usuario))
 else:
  tkinter.messagebox.showerror("mensaje", "Acceso denegado")

ventana = tkinter.Tk()
ventana.title('Login')

labelframe = tkinter.LabelFrame(ventana, text="Login")

# variables
u = tkinter.StringVar()
p = tkinter.StringVar()

#widgets
etiqueta1 = tkinter.Label(labelframe, text="Usuario:")
entrada1 = tkinter.Entry(labelframe, width=18, textvariable = u)
etiqueta2 = tkinter.Label(labelframe, text="Contraseña:")
entrada2 = tkinter.Entry(labelframe, width=18, show="*", textvariable = p)
acceder=tkinter.Button(labelframe, text="Acceder", command = obtener_valores)

# distribución
labelframe.grid(padx=10, pady=10, row=1, column=1)
etiqueta1.grid(row=0, column=1)
entrada1.grid(row=0, column=2, padx=10)
etiqueta2.grid(row=1, column=1)
entrada2.grid(row=1, column=2, padx=10)
acceder.grid(row=4, column=2, pady=8)

ventana.mainloop()
