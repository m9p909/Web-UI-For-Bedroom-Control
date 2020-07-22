#Author: Jack Clarke
import threading, random
import time
debug = False
class Sensors:

    
    def __init__(self):
        self.__temp = 0
        self.__door = False
        self.__sensorThread = threading.Thread
        self.__brightness = 0
        self.__humidity = 0
        self.__startSensorThread()
        self.arduinoConnect = False 


    # public Getters

    def getTemp(self):
        return self.__temp
    def doorIsOpen(self):
        return self.__door
    def getBrightness(self):
        return self.__brightness
    def getHumidity(self):
        return self.__humidity

    #Threading Setup

    def __startSensorThread(self):
        self.__sensorThread = threading.Thread(target=self.__sensorLoop)
        self.__sensorThread.start()
        if debug:
            print("sensors Started")

    def __sensorLoop(self):
        t = threading.currentThread()
        while getattr(t, "do_run", True):
            if debug:
                print("updating")
            self.__updateTemp()
            self.__updateDoor()
            self.__updateBrightness()
            self.__updateHumidity()
            time.sleep(0.1) #really only needs to be around 1 second, but testing is much faster this way
    
    #public Threading commands
    
    # Stops the sensor updater
    def stop(self):
        if self.__sensorThread.is_alive():
            self.__sensorThread.do_run = False
            self.__sensorThread.join()
            if debug:
                print("sensors Stopped")
        else:
            if debug:
                print("Sensors are already stopped")
    #starts the sensor updater
    def start(self):
        if not(self.__sensorThread.is_alive()):
            self.__startSensorThread()
            if debug:
                print("sensor started")
        else:
            if debug:
                print("Sensor is already running")
            
    def isRunning(self):
        return self.__sensorThread.is_alive()
    #Sensor Getters

    #Gets temperature from sensors, not implemented yet, returns dummy values for higher level testing
    #what these function do will depend on if an arduion is used or not
    def __updateTemp(self):
        self.__temp = random.randint(20, 30)
    
    def __updateDoor(self):
        if random.randint(1,5) >=3 :
            self.__door = True
        else:
            self.__door = False
    def __updateBrightness(self):
        self.__brightness = random.randint(200,800)

    def __updateHumidity(self):
        self.__humidity = random.randint(1,100)
    
