import gtk
''' eventos '''


def helloWord(widget):
    print 'Hola mundo \n\t Este es mi primer programa'

def adios(widget):
    gtk.main_quit()
    
''' ventanas '''
ventana = gtk.Window()
ventana.set_title('Hola Mundo')
ventana.set_default_size(400,200)
ventana.connect('destroy', adios)


boton = gtk.Button('Presioname')
boton.connect('clicked', helloWord)

ventana.add(boton)
ventana.show_all()
gtk.main()
	
