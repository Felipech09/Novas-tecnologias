from collections import Counter

numeros = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6]
minimo = 3

contagem = Counter(numeros)

resultado = {num: freq for num, freq in contagem.items() if freq >= minimo}

print(resultado)