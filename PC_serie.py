#------------------- init UART -------------------
import serial #Importation de la bibliothèque « pySerial »
#Création du port lié au COM21 a une vitesse de 115200 bauds
USB_serial = serial.Serial(port= "COM21", baudrate = 115200,timeout = 1) 

USB_serial.close() #Cloture du port pour le cas ou il serait déjà ouvert ailleurs
USB_serial.open() #Ouverture du port
if USB_serial.isOpen():
    print(USB_serial.name + ' is open…')
    print(USB_serial.get_settings())  #affichage des paramètres UART

#---------------Envoi d'un nombre --------------
nombre = int(input("donnez un nombre : "))
USB_serial.write(nombre) #Envoi du nombre
print('nombre envoyé :',nombre)

#----------------Envoi message----------------
message = input("Ecriture un mot : ")
#ser.write(b'hello') #Ecriture de « hello » sur le port
message_serie = message.encode("utf-8") #format bytes
USB_serial.write(message_serie) #Envoi du message
print('message envoyé :',message)

#-------Envoi de variable avec indicateur-----
variable = 45 #exemple nombre ou texte
message  = str(variable) + 'R' #R est un indicateur
message_serie = message.encode("utf-8") #format bytes
USB_serial.write(message_serie) #Envoi du message
print('message envoyé :',message)

#-------Envoi des plusieurs variables ---------
variable1 = 45 #exemple nombre ou texte
variable2 = 78
variable3 = 235
message  = str(variable1) + ' ' + str(variable2) + ' '+str(variable3)
message_serie = message.encode("utf-8") #format bytes
USB_serial.write(message_serie) #Envoi du message
print('message envoyé :',message)

#----------------reception  message----------------
if USB_serial.in_waiting > 0: 
    #Lire le message reçu
    message = USB_serial.readline().decode("utf-8")
    USB_serial.flush() #efface le buffer
    message = message.split(" ")# espace comme separateur
    print(message) #liste
    print(message[0])
