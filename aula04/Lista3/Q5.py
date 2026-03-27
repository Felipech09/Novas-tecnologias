lista1 = [1, 2, 3, 4, 5, 8]
lista2 = [4, 5, 6, 7, 8, 9]

set1 = set(lista1)
set2 = set(lista2)

comuns = set1 & set2
print(f"Valores comuns: {comuns}")

so_na_primeira = set1 - set2
print(f"Só na primeira: {so_na_primeira}")

so_na_segunda = set2 - set1
print(f"Apenas na segunda: {so_na_segunda}")

nao_repetidos = set1 ^ set2
print(f"Elementos não repetidos entre as duas: {nao_repetidos}")

resultado_final = set1 - set2
print(f"Primeira sem repetidos da segunda: {resultado_final}")