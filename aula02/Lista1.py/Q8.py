def codificar(valor):
    lista = list(map(int, str(valor)))
    
    lista = [(x + 7) % 10 for x in lista]
    
    lista = [lista[2], lista[3], lista[0], lista[1]]
    
    return int("".join(map(str, lista)))


def decodificar(valor):
    lista = list(map(int, str(valor)))
    
    lista = [lista[2], lista[3], lista[0], lista[1]]
    
    lista = [(x - 7) % 10 for x in lista]
    
    return int("".join(map(str, lista)))


entrada = int(input("Digite um número de 4 dígitos: "))
codificado = codificar(entrada)
print("Número codificado:", codificado)

decodificado = decodificar(codificado)
print("Número decodificado:", decodificado)

