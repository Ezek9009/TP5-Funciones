"""
 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
 peso en kilogramos y la altura en metros, y devuelva el índice de
 masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun
ción para mostrar el resultado con dos decimales.
"""
#se pide al usuario que ingrese su peso y altura
peso = float(input("ingrese su peso (KG):"))
altura = float(input("ingrese su altura (metros): "))

#se crea la funcion para calcular el IMC
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

#se almacena el return de la funcion en la variable imc
imc = calcular_imc(peso,altura)

#se muestra en pantalla el resultado de IMC
print(f"el indice de masa corporal (IMC) es: {imc:.2f}")