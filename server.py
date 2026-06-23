from flask import Flask, jsonify, request
import mysql.connector

#Conexion a la base de datos
mydb = {
  "host":"localhost",
  "user":"root",
  "password":"",
  "database":"proyectTemperatureHumidity"
}


server= Flask(__name__)

# 1. Crear la ruta para la página principal
@server.route("/")
def hello_world():
    return "Datos de la temperatura y humedad"

# 2. Crear la ruta para obtener los datos del sensor
@server.route("/data/<dataId>")
def dataGet(dataId):
    data = {"id" : dataId, "Temperature": 25, "Humidity": 50}
    return jsonify(data), 200

# 3. Crear la ruta para enviar datos al servidor
@server.route("/data", methods=["POST"])
def dataPost():
    data = request.get_json()
    temperature = data["Temperature"]
    humidity = data["Humidity"]
    print(f"=======Peticion recibida=======\n Temperatura: {temperature}\n Humedad: {humidity}")

    conection = mysql.connector.connect(**mydb)
    cursor = conection.cursor()

    cursor.execute("INSERT INTO measures (temperature, humidity) VALUES (%s, %s)", (temperature, humidity))
    conection.commit()

    cursor.close()
    conection.close()
    print("Datos enviados correctamente")

    return jsonify(data), 201

# 4. Crear la ruta para obtener los datos del sensor
if __name__=="__main__":
    server.run(debug=True, host="0.0.0.0", port=5000)
