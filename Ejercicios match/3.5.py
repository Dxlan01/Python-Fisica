punto = (1, 3)
match punto:
    case (0, y):
        print(f"Esta sobre el eje y en {y}")
    case (x, 0):
        print(f"Esta sobre el eje x en {x}")
    case (x, y):
        print(f"Esta en el punto ({x}, {y})")
    case _:
        print("Patron no reconocido")