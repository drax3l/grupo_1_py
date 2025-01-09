# Saludo inicial
print("BIENVENIDO AL PARQUE DE AVENTURAS".center(50, "="))
nombre = input("¿Cuál es tu nombre? ")
print(f"Hola {nombre}, estamos encantados de recibirte en nuestro Parque de Aventuras.")
print("El precio de la entrada depende de tu edad y de las actividades que elijas disfrutar.")

# Solicitar edad
edad = int(input("¿Cuántos años tienes? "))

# Determinar precio de la entrada
    
if edad < 5:
    print("Tu entrada es gratuita.")
    precio_entrada = 0
elif 5 <= edad <= 12:
    print("Tu entrada cuesta 7€.")
    precio_entrada = 7
elif 13 <= edad <= 17:
    print("Tu entrada cuesta 10€.")
    precio_entrada = 10
else:
    print("Tu entrada cuesta 15€.")
    precio_entrada = 15

# Selección de actividades
print("\nTenemos varias actividades emocionantes para ti:")
print("1. Tirolesa (10€ por persona)")
print("2. Escalada en muro (7€ por persona)")
print("3. Recorrido guiado por la naturaleza (5€ por persona)")
print("4. Circuito de cuerdas (12€ por persona)")
actividad = int(input("¿Qué actividad te gustaría realizar? (Escribe el número de la actividad): "))

# Calcular el costo de la actividad seleccionada
if actividad == 1:
    print("El costo por realizar la tirolesa es 10€.")
    costo_actividad = 10
elif actividad == 2:
    print("El costo por realizar escalada en el muro es 7€.")
    costo_actividad = 7
elif actividad == 3:
    print("El costo por el recorrido guiado es 5€.")
    costo_actividad = 5
elif actividad == 4:
    print("El costo por el circuito de cuerdas es 12€.")
    costo_actividad = 12
else:
    print("Opción no válida. Por favor, elige una actividad válida.")
    costo_actividad = 0

# Preguntar si tiene descuento especial
descuento_especial = input("¿Tienes un cupón de descuento? (Sí/No): ").strip().lower()

# Aplicar descuento si tiene un cupón
if descuento_especial == "sí" or descuento_especial == "si":
    print("¡Genial! Aplicaremos un descuento del 15% sobre el costo total.")
    descuento = 0.15
else:
    descuento = 0

# Calcular el costo total
total = precio_entrada + costo_actividad
total_descuento = total - (total * descuento)

# Mostrar resumen
print("\nResumen de tu compra:")
print(f"Entrada: {precio_entrada}€")
print(f"Actividad seleccionada: {costo_actividad}€")
print(f"Descuento aplicado: {descuento * 100}%")
print(f"Total a pagar: {total_descuento:.2f}€")

# Método de pago
metodo_pago = input("\n¿Qué método de pago deseas utilizar? (Tarjeta/Efectivo): ").strip().lower()

if metodo_pago == "tarjeta":
    print(f"Has elegido pagar con tarjeta. Procesando el pago de {total_descuento:.2f}€...")
elif metodo_pago == "efectivo":
    print(f"Has elegido pagar en efectivo. El total a pagar es {total_descuento:.2f}€.")
else:
    print("Método de pago no válido.")

print("\n¡Gracias por visitarnos! Esperamos que disfrutes de tu tiempo en el Parque de Aventuras.")