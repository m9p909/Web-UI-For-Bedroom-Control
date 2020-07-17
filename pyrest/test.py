import unittest
from Sensors import Sensors
from main import *
import time
class TestSensors(unittest.TestCase):

    def test_init(self):
        sensor = Sensors()
        sensor.stop()

    def test_start(self):
        sensor = Sensors()
        sensor.stop()
        self.assertEqual(sensor.isRunning(),False)
        sensor.start()
        self.assertEqual(sensor.isRunning(),True)
        sensor.stop()
        self.assertEqual(sensor.isRunning(),False)

    def test_Temperature(self):
        sensor = Sensors()
        self.assertEqual(isinstance(sensor.getTemp(),int),True)
        self.assertEqual(sensor.getTemp() > 0,True)
        sensor.stop()
        self.assertEqual(sensor.isRunning(),False)
    
    def test_Humidity(self):
        sensor = Sensors()
        self.assertEqual(isinstance(sensor.getHumidity(),int),True)
        self.assertEqual(sensor.getHumidity() > 0,True)
        sensor.stop()
        self.assertEqual(sensor.isRunning(),False)
    
    def test_Brightness(self):
        sensor = Sensors()
        self.assertEqual(isinstance(sensor.getBrightness(),int),True)
        self.assertEqual(sensor.getBrightness() > 0,True)
        sensor.stop()
        self.assertEqual(sensor.isRunning(),False)
    
    def test_door(self):
        sensor = Sensors()
        self.assertEqual(isinstance(sensor.doorIsOpen(),bool),True)
        sensor.stop()
        self.assertEqual(sensor.isRunning(),False)

class testMain(unittest.TestCase):

    def test_run(self):
        self.assertEqual(isinstance(getTemp(),str),True)
        self.assertEqual(isinstance(getHumidity(),str),True)
        self.assertEqual(isinstance(doorOpen(),str),True)
        self.assertEqual(isinstance(getBrightness(),str),True)

if __name__ == '__main__':
    unittest.main()