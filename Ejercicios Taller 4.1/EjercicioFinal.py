resultados = []
while True:

    print("===== SIMULADOR DE LEYES DE NEWTON =====")
    print("1. Primera Ley - Inercia")
    print("2. Segunda Ley - F = m * a")
    print("3. Tercera Ley - Acción y Reacción")
    print("4. Simular múltiples carritos")
    print("5. Ver resultados")
    print("0. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        print("Primera Ley de Newton")

    elif opcion == 2:

        masa = float(input("Ingrese la masa en kg: "))
        fuerza = float(input("Ingrese la fuerza en N: "))

        if masa > 0:
            aceleracion = fuerza / masa
            resultados.append([masa, fuerza, aceleracion])
            print("Aceleración:", aceleracion, "m/s²")
        else:
            print("La masa debe ser mayor que cero.")

    elif opcion == 3:

        fuerza = float(input("Ingrese la fuerza: "))
        accion = -fuerza
        reaccion = fuerza
        print("Acción:", accion, "N")
        print("Reacción:", reaccion, "N")
        print("← Acción | Reacción →")

    elif opcion == 4:

        fuerzas = [10, 20, 30]
        masa = 5
        mayor = 0

        for i in range(3):

            aceleracion = fuerzas[i] / masa

            print("Carrito", i + 1)
            print("Fuerza:", fuerzas[i], "N")
            print("Aceleración:", aceleracion, "m/s²")

            if aceleracion > mayor:
                mayor = aceleracion

        print("Mayor aceleración:", mayor, "m/s²")

    elif opcion == 5:

        print("===== RESULTADOS =====")

        for i in range(len(resultados)):
            print("Resultado", i + 1)
            print("Masa:", resultados[i][0], "kg")
            print("Fuerza:", resultados[i][1], "N")
            print("Aceleración:", resultados[i][2], "m/s²")

    elif opcion == 0:
        print("Adiós")
        break

    else:
        print("Opción no válida")