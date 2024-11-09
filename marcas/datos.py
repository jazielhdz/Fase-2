import csv

class autos:
    marca = ""
    producto = ""
    precio = ""

    def __init__(self, marca, producto, precio):
        self.marca = marca
        self.producto = producto
        self.precio = precio

lista = [
    ["marca:"],
    ["producto:"],
    ["precio:"]
]

with open("carros.csv", "wt") as archivo:
    print("carros", file = archivo)
    salidacsv = csv.writer (archivo)
    salidacsv.writerows(lista)




