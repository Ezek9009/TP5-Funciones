"""
7. Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resulta
do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re
sultados de forma clara.
"""
#se solicita que ingrese 2 numeros
numero1 = int(input("ingrese primer numero: "))
numero2 = int(input("ingrese segundo numero: "))

#se crea la tupla con las 4 operaciones aritmeticas
def operaciones_basicas(num1, num2):
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = num1 / num2
    tupla = (suma,resta,multiplicacion,division)
    return tupla
    
#almacenamos el return de la funcion en la variable tupla
tupla = operaciones_basicas(numero1,numero2)

#mostramos en pantalla los subindices de la tupla, que son las
#operaciones aritmeticas
print(f"suma = {tupla[0]}")
print(f"resta = {tupla[1]}")
print(f"multiplicacion = {tupla[2]}")
print(f"division = {tupla[3]}")