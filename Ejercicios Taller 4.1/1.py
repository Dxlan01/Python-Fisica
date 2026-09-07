print ("====== LABORATORIO DE NEWTON ======")
while True:
    print ("1. Calcular fuerza\n2. Calcular masa\n3. Calcular aceleración\n0. Salir: ")
    opcion=int(input("Ingrese la opcion: "))
    if opcion == 0:
        print(f"Seleccionado: {opcion}")
        print("Gracias, adios")
        break
    elif opcion == 1:
        masa = float(input("Ingrese la masa: "))
        aceleración = float(input("Ingrese la aceleracion: "))
        fuerza=masa*aceleración
        print(f"Seleccionado: {opcion}")
        print(f"masa: {masa}")
        print(f"aceleracion: {aceleración}")
        print(f"la fuerza es: {fuerza}")
    elif opcion == 2:
        fuerza = float(input("Ingrese la fuerza: "))
        aceleración = float(input("Ingrese la aceleracion: "))
        masa=fuerza/aceleración
        print(f"Seleccionado: {opcion}")
        print(f"fuerza: {fuerza}")
        print(f"aceleracion: {aceleración}")
        print(f"La masa es: {masa}")
    elif opcion == 3:
        masa = float(input("Ingrese la masa: "))
        fuerza = float(input("Ingrese la fuerza: "))
        aceleración = fuerza / masa
        print(f"Seleccionado: {opcion}")
        print(f"masa: {masa}")
        print(f"fuerza: {fuerza}")
        print(f"La aceleracion es: {aceleración}")
    else:
        print("Opción no válida")

