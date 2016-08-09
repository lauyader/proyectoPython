#!/usr/bin/env python
# -*- coding: utf-8 -*-

def calculo():
	print "Convierte medidas inglesas a sistema métrico"
        millas = input("Cuántas millas?:")
        pies = input("Y cuantos pies?:")
	metros = 24*millas+pies
	print "Longitud", metros, "metros" 

calculo()
