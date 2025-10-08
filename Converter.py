class Converter:
    def celsius_to_fahrenheit(self, c):
        if c < -273.15 :
            raise ValueError ("Температура не может быть ниже -273,15С")
        return (c*9/5) + 32
    def fahrenheit_to_celsius(self, f):
        if f < -459.67 :
            raise ValueError("Температура не может быть ниже −459,67F")
        return (f - 32) * 5/9
    def kilometres_to_miles(self , km):
        if km < 0 :
            raise ValueError("Число должно быть положительным")
        return km * 0.621371
    def miles_to_kilometres(self , mi):
        if mi < 0 :
            raise ValueError("Число должно быть положительным")
        return mi / 0.621371