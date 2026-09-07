nombre = input("Ingrese el nombre del vehículo: ")
masa = float(input("Ingrese la masa en kg: "))
fuerza = float(input("Ingrese la fuerza en N: "))

if masa > 0:

    aceleracion = fuerza / masa

    if aceleracion < 2:
        clasificacion = "BAJA"
    elif aceleracion < 5:
        clasificacion = "MEDIA"
    else:
        clasificacion = "ALTA"

    print("===== RESULTADO =====")
    print("Vehículo:", nombre)
    print("Masa:", masa, "kg")
    print("Fuerza:", fuerza, "N")
    print("Aceleración:", aceleracion, "m/s²")
    print("Clasificación:", clasificacion)

else:
    print("La masa debe ser mayor que cero.")