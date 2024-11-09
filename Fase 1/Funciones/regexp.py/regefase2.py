import re
def validar_rfc():
    while True:
        rfc = input("RFC: ")
        if re.match(r"^[A-Z]{3,4}[0-9]{6}[A-Z0-9]{3}$", rfc):
            return rfc
        print("RFC no valido, intente de nuevo")

registro = validar_rfc()
print(registro)
