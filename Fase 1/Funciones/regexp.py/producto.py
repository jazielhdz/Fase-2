import re
def clave_producto():
    while True:
        producto = input("ingrese el numero: ")
        if re.match(r"^[A-Z]{2}-[0-9]{3}$", producto):
            return producto
        print("codigo no valido")

producto = clave_producto()
print(producto)
     


