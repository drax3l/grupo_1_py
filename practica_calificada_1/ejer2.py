"""Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. 
Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no. (10p)
"""

var_edad = int(input("ingrese su edad: "))

var_ingresos = int(input("ingrese sus ingresos mensuales: "))

if var_edad > 16 and var_ingresos > 1000 :
    print("el usuario ya puede tributar!!")
elif var_edad <= 16 and var_ingresos >1000:
    print("el usuario no tiene la edad suficiente para tributar")
elif var_edad > 16 and var_ingresos <1000:
    print("el usuario no cumple el salario optimo para tributar")
else:
    print("el usuario no cumple ninguno de los requisitos!!")


"""while True:
    try:
        var_edad = int(input("Ingrese su edad: "))
        break  # Sale del bucle si la entrada es válida
    except ValueError:
        print("Por favor, ingrese un valor numérico válido para la edad.")

while True:
    try:
        var_ingresos = int(input("Ingrese sus ingresos mensuales: "))
        break  # Sale del bucle si la entrada es válida
    except ValueError:
        print("Por favor, ingrese un valor numérico válido para los ingresos.")

if var_edad > 16 and var_ingresos > 1000:
    print("El usuario ya puede tributar!!")
elif var_edad <= 16 and var_ingresos > 1000:
    print("El usuario no tiene la edad suficiente para tributar")
elif var_edad > 16 and var_ingresos < 1000:
    print("El usuario no cumple el salario óptimo para tributar")
else:
    print("El usuario no cumple ninguno de los requisitos!!")
"""