from sys import platform
import os

class SystemService: 
    
    def __init__(self):
        self.is_arm_linux = False
        if platform == 'linux':
            if "arm" in os.uname().machine:
                self.is_arm_linux = True
  


