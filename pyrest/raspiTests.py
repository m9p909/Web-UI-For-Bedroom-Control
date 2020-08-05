import unittest
from Sensors import Sensors
from main import *
import time
class TestSensors(unittest.TestCase):
    

    def setUpClass():
        sensor = Sensors()
        time.sleep(2)

    def tearDown(self):
        time.sleep(1)

    def test_start(self):
        sensor.start()
        sensor.stop()
        self.assertEqual(sensor.isRunning(),False)
        sensor.start()
        self.assertEqual(sensor.isRunning(),True)
        sensor.stop()
        self.assertEqual(sensor.isRunning(),False)

    def test_Temperature(self):
        sensor.start()
        self.assertEqual(isinstance(sensor.getTemp(),int),True)
        self.assertEqual(sensor.getTemp() > 0,True)
        sensor.stop()
        self.assertEqual(sensor.isRunning(),False)
    
    def test_Humidity(self):
        sensor.start()
        self.assertEqual(isinstance(sensor.getHumidity(),int),True)
        self.assertEqual(sensor.getHumidity() > 0,True)
        sensor.stop()
        self.assertEqual(sensor.isRunning(),False)
    
    def test_Brightness(self):
        sensor.start()
        try:
            self.assertEqual(isinstance(sensor.getBrightness(),int),True)
            self.assertEqual(sensor.getBrightness() > 0,True)
            sensor.stop()
        except:
            print(sensor.getBrightness())
            sensor.stop()
        self.assertEqual(sensor.isRunning(),False)
    
    def test_door(self):
        sensor.start()
        self.assertEqual(isinstance(sensor.doorIsOpen(),bool),True)
        sensor.stop()
        self.assertEqual(sensor.isRunning(),False)
    
    def test_isRaspPi(self):
        sensor.start()
        self.assertEqual(sensor.isRaspberryPi,True)
        sensor.stop()
        self.assertEqual(sensor.isRunning(),False)

class testMain(unittest.TestCase):

    def test_run(self):
        self.assertEqual(isinstance(getTemp(),dict),True)
        self.assertEqual(isinstance(getHumidity(),dict),True)
        self.assertEqual(isinstance(doorOpen(),dict),True)
        self.assertEqual(isinstance(getBrightness(),dict),True)

if __name__ == '__main__':
    unittest.main()
