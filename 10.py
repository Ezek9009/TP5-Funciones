"""
10.Crear una función llamada calcular_promedio(a, b, c) que reciba
 tres números como parámetros y devuelva el promedio de ellos.
 Solicitar los números al usuario y mostrar el resultado usando esta
 función.
"""
#el usuario ingresa 3 numeros
numero1 = int(input("ingrese primer numero: "))
numero2 = int(input("ingrese segundo numero: "))
numero3 = int(input("ingrese tercer numero: "))

#se crea la funcion para calcular el promedio
def calcular_promedio(numero1, numero2, numero3):
    promedio = (numero1 + numero2 + numero3) / 3
    return promedio

#almacenamos el retorno de la funcion en la variable promedio
promedio = calcular_promedio(numero1,numero2,numero3)

#se imprime en pantalla
print(f"el promedio es: {promedio}")