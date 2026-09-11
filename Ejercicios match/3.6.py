class Persona:
    def __init__(self, rol):
        self.rol = rol
p = Persona("admin")
match p:
    case Persona(rol="admin"):
        print("Acceso total")
    case Persona(rol="usuario"):
        print("Acceso limitado")
    case _:
        print("Rol desconocido")