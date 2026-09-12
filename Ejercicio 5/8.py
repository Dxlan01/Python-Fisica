consumos = []
suma=0
for i in range(5):
    consumo = float(input("Ingrese el consumo de la PC: "))
    consumos.append(consumo)
    suma=suma+consumo
promedio=suma/len (consumo)
print("El consumo total de las PC son de:",suma,"\nY el promedio es:",promedio)