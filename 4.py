"""
 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el ra
dio como parámetro y devuelva el área del círculo. calcular_peri
metro_circulo(radio) que reciba el radio como parámetro y devuel
va el perímetro del círculo. Solicitar el radio al usuario y llamar am
bas funciones para mostrar los resultados.
"""
#importamos math, para usar la funcion PI (3,14159)
import math
radio = float(input("ingrese radio del circulo: "))

#se crea la funcion para calcular el area 
def calcular_area_circulo(radio):
    area = math.pi * radio ** 2
    return area

#se crea la funcion para calcular el perimetro
def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    return perimetro

#mostramos en pantalla el resultado del area y perimetro:
print(f"el area del circulo es: {calcular_area_circulo(radio)}")
print(f"el perimetro del circulo es: {calcular_perimetro_circulo(radio)}")