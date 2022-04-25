from sys import platform
import os
from Singleton import SingletonMeta

class SystemService(metaclass=SingletonMeta): 
    def __init__(self):
        if platform == 'linux' and "arm" in os.uname().machine:
            self.is_arm_linux = True
        else:
            self.is_arm_linux = False

    def is_raspi(self):
        return self.is_arm_linux # best guess right now

  


