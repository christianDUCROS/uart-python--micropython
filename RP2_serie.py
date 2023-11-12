from machine import UART, Pin
uart1 = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))

#----------------Envoi message----------------
message = "information1"
message_encode = message.encode("utf-8") #format bytes
uart1.write(message_encode) #Envoi du message
print('message envoyé :',message)

#-------Envoi de variable avec indicateur-----
variable = 45 #exemple nombre ou texte
message_encode = message.encode("utf-8") #format bytes
uart1.write(message_encode) #Envoi du message
print('message envoyé :',message)

#-------Envoi des plusieurs variables ---------
variable1 = 45 #exemple nombre ou texte
variable2 = 78
variable3 = 235
message_encode = message.encode("utf-8") #format bytes
uart1.write(message_encode) #Envoi du message
print('message envoyé :',message)



#----------------reception  message----------------
if uart1.any() > 0: 
    #Lire le message reçu
    message = uart1.read()
    message_decode= message.decode("utf-8")
    print('message reçu :',message_decode) # debug
    
    #-------reception de plusieurs variables séparées par espace---------
    message_decode = message_decode.split(" ") # espace comme separateur
    print(message) # liste
    print(message[0])

'''
#---test reception nombre avant conversion en nombre---
if message_decode[0].isdigit(): 
    valeur1 =  int(message_decode[0])   

'''
