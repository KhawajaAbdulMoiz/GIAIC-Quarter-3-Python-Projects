
# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.

class tempconvertor:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32
celsius_temp = 25
fahrenheit_temp = tempconvertor.celsius_to_fahrenheit(celsius_temp)

print(f"{celsius_temp}°C is equal to {fahrenheit_temp}°F")
