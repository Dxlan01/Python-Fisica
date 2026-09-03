nombre = input("Ingrese el nombre del equipo: ")
masa = float(input("Ingrese la masa (kg): "))
aceleracion = float(input("Ingrese la aceleracion (m/s^2): "))

fuerza = masa * aceleracion

print("=====================================")
print("CALCULADORA DE FUERZA")
print("=====================================")
print(f"Equipo: {nombre}")
print(f"Masa: {masa} kg")
print(f"Aceleracion: {aceleracion} m/s²")
print("RESULTADO")
print(f"Fuerza neta: {fuerza:.0f} N")