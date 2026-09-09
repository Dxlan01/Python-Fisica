fuerzas = []

masa = 5

for i in range(3):
    fuerza = float(input("Ingrese la fuerza: "))
    fuerzas.append(fuerza)

mayor = 0

for i in range(3):
    aceleracion = fuerzas[i] / masa

    print("Carrito", i + 1)
    print("Fuerza:", fuerzas[i], "N")
    print("Aceleración:", aceleracion, "m/s²")

    if aceleracion > mayor:
        mayor = aceleracion

print("Mayor aceleración:", mayor, "m/s²")