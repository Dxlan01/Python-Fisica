Inventario = [1, 12, 4, 3, 14, 1]

for i in range (len(Inventario)):
    if Inventario[i] <= 5:
        print("ATENCION!!! El producto de la posicion ", i+1," esta bajo en stock con solo", Inventario[i], "unidades")
