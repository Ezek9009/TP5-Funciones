"""
5. Crear una función llamada segundos_a_horas(segundos) que reciba
 una cantidad de segundos como parámetro y devuelva la cantidad
 de horas correspondientes. Solicitar al usuario los segundos y mos
trar el resultado usando esta función.
"""

#pedimos al usuario la cantidad de segundos y se guarda en la variable segundos
segundos = int(input("ingrese cantidad de segundos: "))

#se crea la funcion para convertir segundos a horas
def segundos_a_horas(segundos):
    horas = segundos / 60
    return horas

#se imprime en pantalla el resultado
print(f"son {segundos_a_horas(segundos)} horas")