precios=[]
total=0
for i in range(5):
    precio=int(input("Ingrese el precio de los platos pedidos: "))
    precios.append(precio)
    total=total+precio
propina=total*0.1+total
print(f"El total de los platos es de: ",total," Y con una propina del 10% queda en: ",propina)