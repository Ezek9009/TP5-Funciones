"""
2. Crear una función llamada saludar_usuario(nombre) que reciba
 como parámetro un nombre y devuelva un saludo personalizado.
 Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de
volver: “Hola Marcos!”. Llamar a esta función desde el programa
 principal solicitando el nombre al usuario.
"""
#la variable nombre almacena el nombre del usuario a saludar
nombre = input("ingrese su nombre: ")

#la funcion para saludar
def saludar_usuario(nombre):
    return print(f"Hola {nombre}!")

#invocacion de la funcion
saludar_usuario(nombre)