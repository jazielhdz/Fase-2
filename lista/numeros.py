numeros = [39, 40, 41, 42, 43, 44, 45]

indice = int(input("¿cual numero quiere?"))

if 0 <= indice < len(numeros):
    print(numeros[indice])
else:
    print("elemento no valido")
