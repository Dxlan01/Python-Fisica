while True:

    nombre = input("Ingrese el nombre del vehículo: ")
    masa = float(input("Ingrese la masa: "))

    if masa <= 0:
        print("La masa debe ser mayor que cero.")
    else:
        fuerza = float(input("Ingrese la fuerza: "))

        aceleracion = fuerza / masa

        if aceleracion < 2:
            clasificacion = "BAJA"
        elif aceleracion < 5:
            clasificacion = "MEDIA"
        else:
            clasificacion = "ALTA"

        print("Vehículo:", nombre)
        print("Aceleración:", aceleracion, "m/s²")
        print("Clasificación:", clasificacion)

    salir = input("¿Desea salir? (si/no): ")

    if salir == "si":
        break