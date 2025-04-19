"""
 3. Crear una función llamada informacion_personal(nombre, apellido,
 edad, residencia) que reciba cuatro parámetros e imprima: “Soy
 [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe
dir los datos al usuario y llamar a esta función con los valores in
gresados.
"""
#solicitamos al usuario sus datos:
nombre = input("ingrese su nombre: ")
apellido = input("ingrese su apellido: ")
edad = int(input("ingrese su edad: "))
residencia = input("ingrese su pais de residencia: ")

#se crea la funcion para imprimir en pantalla el mensaje
def informacion_personal(nombre, apellido, edad, residencia):
    return print(f"soy {nombre} {apellido}, tengo {edad} y vivo en {residencia} ")

#invocamos la funcion
informacion_personal(nombre,apellido,edad,residencia)