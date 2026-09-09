experimentos = []

mayor = 0
prueba_mayor = 0

for i in range(5):
    masa = float(input("Ingrese la masa: "))
    fuerza = float(input("Ingrese la fuerza: "))

    aceleracion = fuerza / masa

    experimento = [masa, fuerza, aceleracion]
    experimentos.append(experimento)

    if aceleracion > mayor:
        mayor = aceleracion
        prueba_mayor = i + 1

print("===== RESULTADOS DEL EXPERIMENTO =====")

for i in range(5):
    print("Prueba", i + 1)
    print("Masa:", experimentos[i][0], "kg")
    print("Fuerza:", experimentos[i][1], "N")
    print("Aceleración:", experimentos[i][2], "m/s²")

print("Mayor aceleración: Prueba", prueba_mayor)
suma = 0

for i in range(5):
    suma = suma + experimentos[i][2]

promedio = suma / 5

print("Aceleración promedio:", promedio, "m/s²")