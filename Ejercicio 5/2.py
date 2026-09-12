temperaturas = []
mayores_70 = 0
for i in range(5):
    temp = int(input("Ingrese la temperatura del computador: "))
    temperaturas.append(temp)
for i in range(5):
    print("La temperatura del computador", i + 1, "es:", temperaturas[i], "°C")
    if temperaturas[i] > 70:
        mayores_70 = mayores_70 + 1
print("Cantidad de computadores que superan los 70 °C:", mayores_70)