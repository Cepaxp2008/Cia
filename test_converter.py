from Converter import Converter
import unittest

class TestConverter(unittest.TestCase) :
    def setUp(self):
         self.con = Converter()

    def test_celsius_to_fahrenheit(self):
        self.assertEqual(self.con.celsius_to_fahrenheit(0) , 32)
        self.assertEqual(self.con.celsius_to_fahrenheit(77) , 170.6)
        self.assertEqual(self.con.celsius_to_fahrenheit(-25) , -13)
        with self.assertRaises(ValueError):
            self.con.celsius_to_fahrenheit(-400)
    def test_fahrenheit_to_celsius(self):
        self.assertEqual(self.con.fahrenheit_to_celsius(50) , 10)
        self.assertEqual(self.con.fahrenheit_to_celsius(-20), -28.88888888888889)
        with self.assertRaises(ValueError):
            self.con.fahrenheit_to_celsius(-600)
    def test_kilometres_to_miles(self):
        self.assertEqual(self.con.kilometres_to_miles(100) , 62.137100000000004)
        self.assertEqual(self.con.kilometres_to_miles(25), 15.534275000000001)
        with self.assertRaises(ValueError):
            self.con.kilometres_to_miles(-25)
    def test_miles_to_kilometres(self):
        self.assertEqual(self.con.miles_to_kilometres(40) , 64.37377991570253)
        self.assertEqual(self.con.miles_to_kilometres(100), 160.93444978925635)
        with self.assertRaises(ValueError):
            self.con.miles_to_kilometres(-25)
if __name__ == "__main__":
    unittest.main()