from grovepi import * #libreria para el sensor
from grove_rgb_lcd import *   #libreria para la pantalla LCD
import requests #libtreria para enviar informacion del sensor al servidor
from time import sleep 

sensor=7 #pin del sensor
server="http://192.168.1.12:5000/data" #url del servidor

def postSimple(temperature, humidity):
    data = {"Temperature": temperature, "Humidity": humidity} #Datos para enviar al servidor
    sendTest = requests.post(server, json=data) 
    print(sendTest.json()) #Comprobar si se envio correctamente

while True:
    try:

        #Obtener datos del sensor y transformarlos a texto
        [temperature, humidity] = dht(sensor,0)
        textualTemperature = str(temperature)
        textualHumidity = str(humidity)


        #Enviar datos al servidor y mostrarlos en la pantalla LCD
        postSimple(temperature, humidity)
        setText("Temp:" + textualTemperature + "C \n Hum:" + textualHumidity + "%") #Datos para la pantalla LCD
        red=int(255*temperature/35)
        blue=int(255*(100-humidity)/100)
        setRGB(red, 0, blue) #Colores RGB dependiendo de la temperatura y humedad
        sleep(1)

    except (IOError, TypeError) as e:
        print("Error:", e)