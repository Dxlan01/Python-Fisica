nombres = ["Ana", "Pedro", "María", "Carlos", "Sofía"]
notas = [8.5, 4.2, 9.0, 5.8, 7.0]
for i in range(5):
    nombre_estudiante = nombres[i]
    nota_estudiante = notas[i]
    if nota_estudiante >= 6.0:
        estado = "Aprobado"
    else:
        estado = "No aprobado"
    print("Estudiante:", nombre_estudiante, "| Nota:", nota_estudiante, "| Estado:", estado)
