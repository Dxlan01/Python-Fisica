consumos = []
suma=0
for i in range(5):
    consumo = int(input("Ingrese el consumo de la PC: "))
    consumos.append(consumo)
    suma=suma+consumo
promedio=suma/len (consumos)
print("El consumo total de las PC son de:",suma,"Kwh\nY el promedio es:",promedio)