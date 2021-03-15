from reverse import Rever 
from reverIng import IntRever 
from oposite import opposite 

import unittest
import os 

class MyTest(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(type(Rever("rachid")
        ),str)
        self.assertEqual(Rever("rachid"),"dihcar")
if __name__=='__main__':
    unittest.main(verbosity=2)