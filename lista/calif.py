calif = dict()

cant = int(input("cantidad de materias: "))

for _ in range(cant):
    nombre = input("materia: ")
    cal = int(input("calificacion: "))

    calif[nombre] = cal

promedio = sum(list(calif.values())) / len(calif)

for key, value in zip(calif.keys(), calif.values()):
    print(f"{key} {value}")

print(f"promedio: {promedio}")

