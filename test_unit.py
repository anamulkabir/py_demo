import unittest 
from  tddmain import *

class FirstTests(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('code'.upper(),'CODE')
    def test_hello(self):
        self.assertEqual(hello_world(),'Hello World')
    def test_create_num_list(self):
        self.assertEqual(create_num_list(10),list(range(0,10)))
if(__name__ == '__main__'):
    unittest.main()
