#!/usr/bin/python2
 
import pygtk
import gtk
pygtk.require('2.0')
 
class Base:
 def hola(self, widget, data="None"):
  print "hola"
 
 def cerrar_aplicacion(self, widget):
  print "se ha cerrado la aplicacion"
  gtk.main_quit()
 
 def __init__(self):
 
  self.w = gtk.Window(gtk.WINDOW_TOPLEVEL)
  self.w.connect("destroy", self.cerrar_aplicacion)
  self.w.set_title("Ventana de prueba")
  self.w.set_border_width(15)
 
  self.button=gtk.Button("presiona aqui")
  self.button.connect("clicked", self.hola)
 
  self.w.add(self.button)
 
  self.w.show()
  self.button.show()
 
 def principal(self):
  gtk.main()
 
if __name__ == "__main__":
 base = Base()
 base.principal()
