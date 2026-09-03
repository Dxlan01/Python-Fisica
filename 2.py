while True:
    print("==============================")
    print("   SIMULADOR DE MOVIMIENTO")
    print("==============================")
    print("1. Calcular desplazamiento y velocidad media")
    print("2. Calcular aceleración")
    print("0. Salir")
    
    opcion = int(input("Digite la opción que desea realizar: "))

    if opcion == 0:
        print("Saliendo del programa")
        print("Bay")
        break

    elif opcion == 1:
        print("\n DESPLAZAMIENTO Y VELOCIDAD MEDIA ")

        nombre = input("Digite el nombre del vehículo o robot: ")
        posicionInicial = float(input("Digite la posición inicial en metros: "))
        posicionFinal = float(input("Digite la posición final en metros: "))
        tiempo = float(input("Digite el tiempo en segundos: "))

        desplazamiento = posicionFinal - posicionInicial
        velocidadMedia = desplazamiento / tiempo

        print("\n================================")
        print(" SIMULADOR DE MOVIMIENTO")
        print("================================")
        print("Robot:", nombre)
        print("Posición inicial:", posicionInicial, "m")
        print("Posición final:", posicionFinal, "m")
        print("Tiempo:", tiempo, "s")
        print("RESULTADOS")
        print("Desplazamiento:", desplazamiento, "m")
        print("Velocidad media:", velocidadMedia, "m/s")

    elif opcion == 2:
        print("\n CÁLCULO DE ACELERACIÓN ")

        velocidadInicial = float(input("Digite la velocidad inicial en m/s: "))
        velocidadFinal = float(input("Digite la velocidad final en m/s: "))
        tiempo = float(input("Digite el tiempo en segundos: "))

        aceleracion = (velocidadFinal - velocidadInicial) / tiempo

        print("\n================================")
        print("     CÁLCULO DE ACELERACIÓN")
        print("================================")
        print("Velocidad inicial:", velocidadInicial, "m/s")
        print("Velocidad final:", velocidadFinal, "m/s")
        print("Tiempo:", tiempo, "s")
        print("RESULTADO")
        print("Aceleración:", aceleracion, "m/s²")

    else:
        print("Opción no válida")