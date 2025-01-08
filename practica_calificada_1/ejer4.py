"""Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere
calcular de forma automática el precio que debe cobrar a sus clientes por entrar.
El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada.
Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€. (10p)"""

print("bienvenido a la sala de juegos".upper())
valor_nombre= input("cual es tu nombre: ")
print("el precio de los juegos varia dependiendo la edad")
valor_edad = int(input("cual es tu edad: "))
if valor_edad < 4:
    print(f"hola {valor_nombre} es un gusto que vengas a nuestra sala de juegos")
    print("su entrada es gratuita")
elif 4<= valor_edad <= 18:
    print(f"hola {valor_nombre} es un gusto que vengas a nuestra sala de juegos")
    print("su entrada costara 5€")
elif valor_edad > 18:
    print(f"hola {valor_nombre} es un gusto que vengas a nuestra sala de juegos")
    print("su entrada costara 10€")
else:
    print("ups ocurrio un error, pruebe usar una edad valida!!")
