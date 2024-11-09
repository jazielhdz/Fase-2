contactos = list()

while True:
    usuario = input("nombre del usuario: ")
    telefono = int (input("numero de telefono: "))
    correo = input("ingrese su correo electronico: ")   
    contactos.append({'nombre': usuario, 'telefono': telefono, 'ingrese': correo})

    salir = input("presiona L para continuar, presione cualquier tecla para avanzar")

    if salir.upper() == "L":
        break

for elem in contactos:
    print(f"{elem['nombre']}: {elem['telefono']}: {elem['correo']}")

