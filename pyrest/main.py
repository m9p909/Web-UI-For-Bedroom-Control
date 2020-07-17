from flask import Flask
from Sensors import Sensors
app = Flask(__name__)
sensor = Sensors()

@app.route("/temp")
def getTemp():
    return str(sensor.getTemp())

@app.route("/door")
def doorOpen():
    return str(sensor.doorIsOpen())

@app.route("/brightness")
def getBrightness():
    return str(sensor.getBrightness())

@app.route("/humidity")
def getHumidity():
    return str(sensor.getHumidity())

if(__name__ == '__main__'):
    app.run(port=808)