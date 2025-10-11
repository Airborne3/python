class Converter:
    @staticmethod
    def celsius_to_fahrenheit(c):

        return c * 9 / 5 + 32

    @staticmethod
    def fahrenheit_to_celsius(f):

        return (f - 32) * 5 / 9

    @staticmethod
    def kilometers_to_miles(km):

        return km * 0.621371

    @staticmethod
    def miles_to_kilometers(mi):

        return mi / 0.621371