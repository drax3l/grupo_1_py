# Saludo inicial
print("BIENVENIDO AL PARQUE DE AVENTURAS".center(50, "="))
nombre = input("¿Cuál es tu nombre?: ")
print(f"Hola {nombre}, estamos encantados de recibirte en nuestro Parque de Aventuras.")
print("El precio de la entrada depende de tu edad y de las actividades que elijas disfrutar.")

# Solicitar edad
edad = int(input("¿Cuántos años tienes?: "))

# Determinar precio de la entrada
if edad < 5:
    print("Tu entrada es gratuita.")
    precio_entrada = 0
elif 5 <= edad <= 12:
    print("Tu entrada cuesta S/.7")
    precio_entrada = 7
elif 13 <= edad <= 17:
    print("Tu entrada cuesta S/.10")
    precio_entrada = 10
else:
    print("Tu entrada cuesta S/.15")
    precio_entrada = 15

# Mostrar actividades disponibles
print("\nTenemos varias actividades emocionantes para ti:")
print("1. Tirolesa (S/.10 por persona)")
print("2. Escalada en muro (S/.7 por persona)")
print("3. Recorrido guiado por la naturaleza (S/.5 por persona)")
print("4. Circuito de cuerdas (S/.12 por persona)")

# Preguntar cuántas actividades desea realizar
cantidad_actividades = int(input("¿Cuántas actividades deseas realizar?: "))

# Inicializar costo total de actividades
costo_actividades = 0

# Usar ciclo for para registrar las actividades
for i in range(cantidad_actividades):
    actividad = int(input(f"Selecciona la actividad {i + 1} (Escribe el número de la actividad): "))
    
    # Determinar el costo de cada actividad
    if actividad == 1:
        print("Has elegido la tirolesa. Costo: S/.10")
        costo_actividades += 10
    elif actividad == 2:
        print("Has elegido escalada en el muro. Costo: S/.7")
        costo_actividades += 7
    elif actividad == 3:
        print("Has elegido el recorrido guiado. Costo: S/.5")
        costo_actividades += 5
    elif actividad == 4:
        print("Has elegido el circuito de cuerdas. Costo: S/.12")
        costo_actividades += 12
    else:
        print("Opción no válida. No se sumará ninguna actividad.")

# Preguntar si tiene descuento especial
descuento_especial = input("¿Tienes un cupón de descuento? (Sí/No): ").strip().lower()

# Aplicar descuento si tiene un cupón
if descuento_especial == "sí" or descuento_especial == "si":
    print("¡Genial! Aplicaremos un descuento del 15% sobre el costo total.")
    descuento = 0.15
else:
    descuento = 0

# Calcular el costo total
total = precio_entrada + costo_actividades
total_descuento = total - (total * descuento)

# Mostrar resumen
print("\nResumen de tu compra:")
print(f"Entrada: S/.{precio_entrada}")
print(f"Costo total de actividades: S/.{costo_actividades}")
print(f"Descuento aplicado: {descuento * 100}%")
print(f"Total a pagar: S/.{total_descuento:.2f}")

# Método de pago
metodo_pago = input("\n¿Qué método de pago deseas utilizar? (Tarjeta/Efectivo): ").strip().lower()

if metodo_pago == "tarjeta":
    print(f"Has elegido pagar con tarjeta. Procesando el pago de S/.{total_descuento:.2f}...")
elif metodo_pago == "efectivo":
    print(f"Has elegido pagar en efectivo. El total a pagar es S/.{total_descuento:.2f}.")
else:
    print("Método de pago no válido.")

print("\n¡Gracias por visitarnos! Esperamos que disfrutes de tu tiempo en el Parque de Aventuras.")