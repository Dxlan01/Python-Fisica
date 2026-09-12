notas = []
suma=0
for i in range(5):
    nota = float(input("Ingrese la nota del aprendiz: "))
    notas.append(nota)
    suma=suma+nota
promedio=suma/len (notas)
if(promedio>=3.0):
    print("El estudiante aprobo")
else:
    print("El estudiante reprobo")