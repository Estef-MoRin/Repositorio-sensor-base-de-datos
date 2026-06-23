from flask import Flask, jsonify, request
import mysql.connector

#Conexion a la base de datos
mydb = {
  "host":"localhost",
  "user":"root",
  "password":"",
  "database":"proyectTemperatureHumidity"
}
