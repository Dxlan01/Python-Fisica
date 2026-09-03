while True:
    print("==============================")
    print("      ANALISIS DE ROBOTS")
    print("==============================")
    print("1. Rapidez de los robots")
    print("2. Robot más rápido")
    print("3. Robot más lento")
    print("4. Rapidez promedio")
    print("5. Ordenar de mayor a menor")
    print("0. Salir")

    opcion = int(input("Digite una opción: "))

    if opcion == 0:
        print("Saliendo del programa")
        break

    elif opcion == 1:
        R01 = 100 / 20
        R02 = 150 / 25
        R03 = 80 / 20
        R04 = 200 / 40
        R05 = 120 / 20

        print("Rapidez R01:", R01, "m/s")
        print("Rapidez R02:", R02, "m/s")
        print("Rapidez R03:", R03, "m/s")
        print("Rapidez R04:", R04, "m/s")
        print("Rapidez R05:", R05, "m/s")

    elif opcion == 2:
        print("El robot más rápido es R02 y R05")
        print("Rapidez: 6 m/s")

    elif opcion == 3:
        print("El robot más lento es R03")
        print("Rapidez: 4 m/s")

    elif opcion == 4:
        promedio = (5 + 6 + 4 + 5 + 6) / 5
        print("La rapidez promedio es:", promedio, "m/s")

    elif opcion == 5:
        print("Robots de mayor a menor rapidez:")
        print("R02 - 6 m/s")
        print("R05 - 6 m/s")
        print("R01 - 5 m/s")
        print("R04 - 5 m/s")
        print("R03 - 4 m/s")

    else:
        print("Opción no válida")