#!/usr/bin/python
import serial
import syslog
import serial

ser = serial.Serial("/dev/ttyACM0", 9600)
while True:
    #print ser.readline()
    datos=ser.readline()
    print datos
