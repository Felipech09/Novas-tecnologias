def existe_soma(lista, alvo):
    if alvo == 0:
        return True
    
    if not lista:
        return False

    primeiro = lista[0]
    resto_da_lista = lista[1:]

    if existe_soma(resto_da_lista, alvo - primeiro):
        return True

    if existe_soma(resto_da_lista, alvo):
        return True
    return False

print(existe_soma([3, 34, 4, 12, 5, 2], 9))