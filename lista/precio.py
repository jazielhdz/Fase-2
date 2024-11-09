precios = {'leche': 23.0, 'aceite': 40.0, 'arroz': 28.0, 'huevo': 54.00}

producto = input("producto: ")
cantidad = int(input("cantidad: "))
precio = precios.get(producto, 0)

if precio > 0:
    venta = cantidad * precio 
    print(f"venta: $ {venta}")
else:
    print("no existe el producto")