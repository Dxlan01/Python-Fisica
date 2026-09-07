print ("====== CARRERA DE CARRITOS ======")
fuerzas = [10, 20, 30]
masa = 5

mayor = 0
carrito_mayor = ""

for i in range(3):
    aceleracion = fuerzas[i] / masa

    print("Carrito", i + 1)
    print("Fuerza:", fuerzas[i], "N")
    print("Aceleración:", aceleracion, "m/s²")

    if aceleracion > mayor:
        mayor = aceleracion
        carrito_mayor = i + 1

print("Mayor aceleración: Carrito", carrito_mayor)
