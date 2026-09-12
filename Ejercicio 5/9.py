dias_retraso = [0, 5, 0, 12, 3, 0]
numero_prestamo = 1
aldia = 0
print("Préstamos con retraso:")
for dias in dias_retraso:
    if dias > 0:
        print(" -Préstamo",numero_prestamo,":", dias, "días de retraso")
    else:
        aldia = aldia + 1
    numero_prestamo = numero_prestamo + 1
print("\nCantidad de préstamos que están al día:", aldia)
