calif = list ()

while True:
    materia = input("Nombre de la materia: ")
    cal = int (input("calificacion: "))
    calif.append({'materia': materia, "calificacion": cal})

    salir = input("Presione L para salir, para avanzar presione cualquier tecla")

    if salir.upper() == "L":
        break

for elem in calif:
    print(f"{elem['materia']}: {elem['calificacion']}")