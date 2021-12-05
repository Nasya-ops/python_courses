import unittest
from hello import greet

class TestHello(unittest.TestCase):

    def test_greet(self):
        self.assertEqual(greet('Hi'), 'Hello world!')

    def test_type(self):
        self.assertRaises(TypeError,greet, 3)
        self.assertRaises(TypeError, greet,True)
        self.assertRaises(TypeError, greet, [4])