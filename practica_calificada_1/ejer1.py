"""Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida 
por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas. (10 p)
"""

programa = "contraseña"
contraseña = (input("por favor ingrese la contraseña: ")).lower()
if contraseña == programa:
    print("la contraseña es correcta")
    
else:
    print("contraseña incorrecta")



