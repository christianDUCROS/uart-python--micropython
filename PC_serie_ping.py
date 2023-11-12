# Test PING liaison série coté PC
# maitre : PC    escalve : raspberry pi pico

#------------------- init UART -------------------
import serial #Importation de la bibliothèque « pySerial »
#Création du port lié au COM21 a une vitesse de 115200 bauds
USB_serial = serial.Serial(port= "COM6", baudrate = 115200,timeout = 1) 

USB_serial.close() # Cloture du port pour le cas ou il serait déjà ouvert ailleurs
USB_serial.open() # Ouverture du port
if USB_serial.isOpen():
    print(USB_serial.name + ' is open…')

import time # mesure des pings
import random # chiffre aléatoire dans al'envoi des pings
########################################################################
 #--------------4-Pings  --------------
for i in range (4) :
    nombre = random.randint(0,100)
    message = str(nombre)
    message_encode = message.encode()
    start_time = time.time()  # start du ping
    USB_serial.write(message_encode)
    while USB_serial.in_waiting == 0:
        pass
    delta_time = time.time() - start_time # fin mesure ping
    message = USB_serial.readline()
    message_decode = message.decode()
    USB_serial.flush() # efface le buffer
    if message_decode == str(nombre) : 
        print('Ping numero : ',i+1, ', temps : ',delta_time)
    else :
        print('Erreur Ping numero : ',i+1)
    time.sleep(1) # delai entre 2 pings
       