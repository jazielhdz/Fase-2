import json

class autos:
    marca = ""
    producto = ""
    precio = ""

    def __init__(self, marca, producto, precio):
        self.marca = marca
        self.producto = producto
        self.precio = precio
      

auto = []
auto.append(autos("marca"))
auto.append(autos("producto"))
auto.append(autos("precio"))

print(auto)
json_data = json.dumps(auto, default=lambda o: o.__dict__, indent=4, ensure_ascii=False)

with open("auto.json", "wt") as archivo:
    print(json_data, file=archivo)
