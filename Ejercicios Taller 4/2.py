nombre = input("Ingrese el nombre del equipo: ")
masa = float(input("Ingrese la masa (kg): "))
aceleracion = float(input("Ingrese la aceleracion (m/s^2): "))
f_entrada = float(input("Ingrese la fuerza de entrada (N): "))
f_salida = float(input("Ingrese la fuerza de salida (N): "))

fuerza = masa * aceleracion
peso = masa * 9.8
vm = f_salida / f_entrada

print("=====================================")
print("ANÁLISIS FÍSICO DEL EQUIPO")
print("=====================================")
print(f"Equipo: {nombre}")
print(f"Masa: {masa} kg")
print(f"Aceleracion: {aceleracion} m/s²")
print(f"Fuerza: {fuerza:.0f} N")
print(f"Peso: {peso:.0f} N")
print(f"Fuerza de entrada: {f_entrada:.0f} N")
print(f"Fuerza de salida: {f_salida:.0f} N")
print(f"Ventaja mecanica: {vm:.0f}")