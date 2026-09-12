nota = int(input("Ingrese la nota: "))
match nota:
    case n if n >= 90:
        print("Excelente")
    case n if 70 <= n < 90:
        print("Aprobado")
    case n if 50 <= n <70:
        print("En recuperacion")
    case _:
        print("Reprobado")