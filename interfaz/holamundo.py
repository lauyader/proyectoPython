import pygtk
pygtk.require('2.0')
import gtk



def hello(widget):
	print "Hola mundo \n"


def quit(widtget):
	gtk.main_quit()


#Creamos la ventana y agregamos sus propiedades

window = gtk.Window(gtk.WINDOW_TOPLEVEL)
window.set_default_size(300,200)
window.connect("destroy",quit)


#button = gtk.Button("Presioname")
#button.connect("Clicked", hello)

