from flask import Flask
from Sensors import Sensors
app = Flask(__name__)
sensor = Sensors()

@app.route("/temp")
def getTemp():
    item = {
        "data": sensor.getTemp()
    }
    return item

@app.route("/door")
def doorOpen():
    item = {
        "data": sensor.doorIsOpen()
    }
    return item


@app.route("/brightness")
def getBrightness():
    item = {
        "data": sensor.getBrightness()
    }
    return item


@app.route("/humidity")
def getHumidity():
    item = {
        "data": sensor.getHumidity()
    }
    return item

@app.route("/all")
def getAllSensorData():
    item={
        "data": sensor.getAllSensorData()
        

    }
    return item

if(__name__ == '__main__'):
    app.run(port=808)
