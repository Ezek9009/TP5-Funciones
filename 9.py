"""
9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
 una temperatura en grados Celsius y devuelva su equivalente en
 Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
 resultado usando la función.
"""

grados_celsius = float(input("ingrese grados celsius: "))

def celsius_a_fahrenheit(celsius):
    farenheit = (celsius * 1.8) + 32
    return farenheit

conversion = celsius_a_fahrenheit(grados_celsius)
print(f"grados celsius({grados_celsius}°C) a fahrenheit = {conversion} °F")