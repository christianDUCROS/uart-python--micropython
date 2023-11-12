# Test PING liaison série coté Raspberry pi-pico
# maitre : PC    escalve : raspberry pi pico 
#------------------- init UART -------------------from machine import UART, Pin
from machine import UART, Pin
uart1 = UART(1, baudrate=115200, tx=Pin(4), rx=Pin(5))

########################################################################

while True :
    if uart1.any()>0 : 
        message = uart1.read()
        uart1.write(message) #pas d'encodage car nombre
        message_decode = message.decode()
        print('message envoyé : ' ,message_decode)
    