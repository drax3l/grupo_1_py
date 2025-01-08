"Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde. (10p)"

renta = input("ingrese el monto de su renta anual: ")
if renta < 10000:
    print("su tipo impositivo es del 5%")
elif 10000< renta < 20000:
    print("su tipo impositivo es del 15%")
elif 20000 < renta < 35000:
    print("su tipo impositivo es del 20%")
elif 35000 < renta < 60000:
    print("su tipo impositivo es del 30%")
elif renta > 60000:
    print("su tipo impositivo es del 45%")
else:
    print("ocurrio un error, ingrese valores validos!!")
    