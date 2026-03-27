def mesclar_intervalos(intervalos):
    if not intervalos:
        return []

    intervalos.sort(key=lambda x: x[0])

    mesclados = [intervalos[0]]

    for atual_inicio, atual_fim in intervalos[1:]:
        ultimo_inicio, ultimo_fim = mesclados[-1]

        if atual_inicio <= ultimo_fim:
            mesclados[-1] = (ultimo_inicio, max(ultimo_fim, atual_fim))
        else:
            mesclados.append((atual_inicio, atual_fim))

    return mesclados

entrada = [(1, 4), (2, 5), (7, 9)]
resultado = mesclar_intervalos(entrada)
print(f"Entrada: {entrada}")
print(f"Saída:   {resultado}")