class Producto:
    clave = ""
    nombre = ""
    costo = 0
    precio = 0
    unidades = 0
    marca = ""

    def __init__(self, clave, nombre, marca):
        self.clave = clave
        self.nombre = nombre
        self.marca = marca

    def compra(self, aumento):
        self.unidades += aumento
        

    def venta(self, disminucion): 
        self.unidades -= disminucion 
    if 

        

        



