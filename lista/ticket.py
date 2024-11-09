b = dict()
print(b)

cant = int(input("cantidad de articulos: "))

for _ in range (cant):
    producto = input("producto: ")
    costo = int(input("precio: "))

    b[producto] = costo

total = sum(list(b.values())) 

for key, value in zip (b.keys(), b.values()):
    print(f"{key}, {value}")

print(f"total: {total}")
