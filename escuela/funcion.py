from clases import estudiante

def get_datos():
    matricula = input("matricula: ")
    nombre = input("nombre: ")
    apellidos = input("apellidos: ")

    return estudiante(matricula, nombre, apellidos)

def llenar_lista(estudiantes: list):
    while True:
        estudiante = get_datos()
        estudiantes.append(estudiante)

        salir = input("presione L para salir o cualquier tecla para continuar")
        if salir.upper() == "L":
            break