import unittest
from SystemService import SystemService

import main


class MainUnittest(unittest.TestCase):

    
    def test_returns_platform_pi(self):
        if(SystemService().is_raspi()):
            self.assertEquals(main.getPlatform(), {"platform": "pi"})
        else:
            self.assertEquals(main.getPlatform(),{"platform": "other"} )


if __name__ == "__main__":
    unittest.main()
