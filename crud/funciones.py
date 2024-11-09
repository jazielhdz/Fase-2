def get_int(s: str)-> int:
    while True:
        num = input(f"{s}: ")
        try: 
            num = int(num)
            return num
        except ValueError:
            print("debe ingresar un numero entero")

def pide_datos() -> dict:
    matricula = get_int("matricula")
    nombre = input("nombre: ")
    apellidos = input("apellidos: ")

    return {"matricula": matricula, "nombre": nombre, "apellidos": apellidos}

def mostrar_datos(L: list) -> None:
    for e in L:
        print(f"{e["matricula"]} {e["nombre"]} {e["apellidos"]}")

def buscar(e: list) -> int:
    m = get_int("matricula")

    for i in range(len(e)):
        if e[i]["matricula"] == m:
            return i
    return -1

def mostrar_dato(e: list) -> None:
    i = buscar(e)
    if i >= 0:
        print(f"{e[i]["matricula"]} {e[i]["nombre"]} {e[i]["apellidos"]}")
    else:
        print("la matricula no existe")

def registrar(e: list) -> None:
    while True: 
        e.append(pide_datos())

        salir = input("escriba x para salir o cualquier tecla para continuar")
        if salir.upper() == "x":
            break

def eliminar(e: list) -> None:
    i = buscar(e)

    if i >= 0:
        e.pop(i)
    else:
        print("no existe el numero de matricula")

def modificar(e: list) -> None:
    while True:
        idx = buscar(e)
        if idx > 0:
            break
        else:
            print("no existe el estudiante, ingrese otra matricula")

    nombre = input("nombre: ")
    apellidos = input("apellidos: ")

    e[idx]["nombre"] = nombre
    e[idx]["apellidos"] = apellidos

def menu() -> int:
    while True:
        print("[1] pide datos")
        print("[2] mostrar dato")
        print("[3] mostrar datos")
        print("[4] registrar") 
        print("[5] modificar")
        print("[6] eliminar")
        print("[7] salir")
