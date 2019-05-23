##client.py

from opcua import Client
import time
from random import randint



url = "opc.tcp://localhost:49320"     #Server IP and port
client = Client(url)

client.connect()
print("Client Connected")
try:
    while True:

        Temp = client.get_node("ns=2;i=2")
        Temperature = Temp.get_value()
        print('S_Temp = {0}'.format(Temperature))
        Tempe = randint(10,50)
        print('C_Temp = {0}'.format(Tempe))
        Temp.set_value(Tempe)

        Press = client.get_node("ns=2;i=3")
        Pressure = Press.get_value()
        print('S_Press = {0}'.format(Pressure))
        Pressu = randint(200,999)
        print('C_Temp = {0}'.format(Pressu))
        Press.set_value(Pressu)

        TIME = client.get_node("ns=2;i=4")
        TIME_value = TIME.get_value()
        print(TIME_value)

        time.sleep(2)
finally:
    client.disconnect()
