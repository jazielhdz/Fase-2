nombres_lista = []

cantidad = int(input("cantidad de nombres: ")) 

for i in range(cantidad):
    nombres = input(f"ingresa el nombre {i + 1}: ")
    nombres_lista.append(nombres)

print("los nombres ingresados son: ")
for nombres in nombres_lista:
    print(nombres)


