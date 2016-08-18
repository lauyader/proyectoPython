from Tkinter import *

w = Tk()

l = Label(w, text='Etiqueta')
l.pack()

b = Button(w, text='Boton')
b.pack()

e = Entry(w)
e.pack()


scale_widget = Scale(w, from_=0, to=100, orient=HORIZONTAL)
scale_widget.set(25)
scale_widget.pack()

'''scale_widget = Scale(w, from=0, to=100, orient=VERTICAL)
scale_widget.set(26)
scale_widget.pack()
'''
w.mainloop()
