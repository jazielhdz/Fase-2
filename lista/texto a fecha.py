from datetime import datetime

def validar_fecha():
    while True:
        dato = input ("ingrese la fecha en formato dd-mm-aaaa")
        try: 
            dato = datetime.strptime(dato, "%d-%m-%Y")
            return dato 
        except ValueError:
            print("ingrese una fecha valida")

fecha = validar_fecha()
print(type (fecha))
