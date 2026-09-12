numero_dia = 6
match numero_dia:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miercoles")
    case 4 | 5 :
        print("Entre semana")
    case 6 | 7:
        print("Fin de semana")
    case _:
        print("Numero no valido")