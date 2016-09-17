
#Ejemplo de deteccion facial con OpenCV y Python

#Por Glare

#www.robologs.net


import numpy as np

import cv2


#cargamos la plantilla e inicializamos la webcam:

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

cap = cv2.VideoCapture(0)


while(True):

    #leemos un frame y lo guardamos

    ret, img = cap.read()


    #convertimos la imagen a blanco y negro
