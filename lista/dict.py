nombre = input("nombre completo: ")
edad = int(input("edad: "))
direccion = input("direccion:")
telefono = input("telefono: ")

datos = {"nombre": nombre, "edad": edad, "direccion": direccion, "telefono": telefono}

print(f"{datos["nombre"]} tiene {datos["edad"]} años, con domicilio en {datos["direccion"]} y su numero telefonico es {datos["telefono"]}")
