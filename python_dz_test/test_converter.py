import unittest
from converter import Converter


class TestConverter(unittest.TestCase):

    def test_celsius_to_fahrenheit(self):
        self.assertAlmostEqual(Converter.celsius_to_fahrenheit(0), 32.0)
        self.assertAlmostEqual(Converter.celsius_to_fahrenheit(100), 212.0)
        self.assertAlmostEqual(Converter.celsius_to_fahrenheit(-40), -40.0)
        self.assertAlmostEqual(Converter.celsius_to_fahrenheit(37), 98.6, places=1)

    def test_fahrenheit_to_celsius(self):
        self.assertAlmostEqual(Converter.fahrenheit_to_celsius(32), 0.0)
        self.assertAlmostEqual(Converter.fahrenheit_to_celsius(212), 100.0)
        self.assertAlmostEqual(Converter.fahrenheit_to_celsius(-40), -40.0)
        self.assertAlmostEqual(Converter.fahrenheit_to_celsius(98.6), 37.0, places=1)

    def test_kilometers_to_miles(self):
        self.assertAlmostEqual(Converter.kilometers_to_miles(0), 0.0)
        self.assertAlmostEqual(Converter.kilometers_to_miles(1), 0.621371)
        self.assertAlmostEqual(Converter.kilometers_to_miles(10), 6.21371)
        self.assertAlmostEqual(Converter.kilometers_to_miles(-5), -3.106855)

    def test_miles_to_kilometers(self):
        self.assertAlmostEqual(Converter.miles_to_kilometers(0), 0.0)
        self.assertAlmostEqual(Converter.miles_to_kilometers(1), 1.609344, places=6)
        self.assertAlmostEqual(Converter.miles_to_kilometers(10), 16.09344, places=5)
        self.assertAlmostEqual(Converter.miles_to_kilometers(-5), -8.04672, places=5)


    def test_temperature_roundtrip(self):
        c = 25.0
        f = Converter.celsius_to_fahrenheit(c)
        c_back = Converter.fahrenheit_to_celsius(f)
        self.assertAlmostEqual(c, c_back)

    def test_distance_roundtrip(self):
        km = 100.0
        mi = Converter.kilometers_to_miles(km)
        km_back = Converter.miles_to_kilometers(mi)
        self.assertAlmostEqual(km, km_back, places=6)


if __name__ == '__main__':
    unittest.main()