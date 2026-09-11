edades=[]
contM=0
contm=0
for i in range(8):
    edad=int(input("Ingrese la edad: "))
    edades.append(edad)
    if(edades[i]>=18):
        contM+=1
    elif(edades[i]<18):
        contm+=1
print("Las personas mayores de edad son:",contM,"\nLas personas menores de edad son:",contm)