from machine import UART, Pin
uart1 = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))

#----------------Envoi message----------------
message = "information1"
message_serie = message.encode("utf-8") #format bytes
uart1.write(message_serie) #Envoi du message
print('message envoyé :',message)

#---------------Envoi d'un nombre --------------
nombre = 45
uart1.write(nombre) #Envoi du nombre
print('nombre envoyé :',nombre)

#-------Envoi de variable avec indicateur-----
variable = 45 #exemple nombre ou texte
message_serie = message.encode("utf-8") #format bytes
uart1.write(message_serie) #Envoi du message
print('message envoyé :',message)

#-------Envoi des plusieurs variables ---------
variable1 = 45 #exemple nombre ou texte
variable2 = 78
variable3 = 235
message_serie = message.encode("utf-8") #format bytes
uart1.write(message_serie) #Envoi du message
print('message envoyé :',message)



#----------------reception  message----------------
if uart1.any() > 0: 
    #Lire le message reçu
    message = uart1.read().decode("utf-8")
    message = message.split(" ")# espace comme separateur
    print(message) #liste
    print(message[0])



'''
#---test reception nombre avant conversion en nombre---
if message[0].isdigit(): 
    valeur1 =  int(message[0]   
'''