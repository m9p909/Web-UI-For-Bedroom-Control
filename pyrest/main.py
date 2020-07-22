#Author: Jack Clarke
from flask import Flask
from Sensors import Sensors
app = Flask(__name__)
sensor = Sensors()

@app.route("/temp")
def getTemp():
    item = {
        "temp": sensor.getTemp()
    }
    return item

@app.route("/door")
def doorOpen():
    item = {
        "doorIsOpen": sensor.doorIsOpen()
    }
    return item


@app.route("/brightness")
def getBrightness():
    item = {
        "brightness": sensor.getBrightness()
    }
    return item


@app.route("/humidity")
def getHumidity():
    item = {
        "humidity": sensor.getHumidity()
    }
    return item


if(__name__ == '__main__'):
    app.run(port=808)
