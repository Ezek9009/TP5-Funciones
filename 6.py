"""
6. Crear una función llamada tabla_multiplicar(numero) que reciba un
 número como parámetro y imprima la tabla de multiplicar de ese
 número del 1 al 10. Pedir al usuario el número y llamar a la fun
ción."""
#solicitamos un numero al usuario
numero = int(input("ingrese un numero: "))

#se crea la funcion para mostrar la tabla de multiplicar
def tabla_multiplicar(numero):
    for i in range(1,11):
        print(f"{numero} * {i} = {i * numero}")

#invocamos la funcion
tabla_multiplicar(numero)