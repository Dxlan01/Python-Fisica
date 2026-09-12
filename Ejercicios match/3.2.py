dia = "Viernes"
match dia:
    case "Lunes":
        print("Inicio de semana")
    case "Martes" | "Miercoles" | "Jueves":
        print("Dia laboral")
    case "Viernes":
        print("¡Viernes!")
    case "Sabado" | "Domingo":
        print("Fin de semana")
    case _:
        print("Dia no valido")