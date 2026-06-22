from grovepi import * #libreria para el sensor
from time import sleep 

sensor=7 #pin del sensor

def postSimple(temperature, humidity):
    data = {"Temperature": temperature, "Humidity": humidity} 

while True:
    try:

        #Obtener datos del sensor y transformarlos a texto
        [temperature, humidity] = dht(sensor,0)
        textualTemperature = str(temperature)
        textualHumidity = str(humidity)



    except (IOError, TypeError) as e:
        print("Error:", e)