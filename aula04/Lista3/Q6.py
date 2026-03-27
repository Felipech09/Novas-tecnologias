tamanho = 1000
array = [1] * tamanho

for i in range(2, tamanho):
    if array[i] == 1:
        for multiplo in range(i * 2, tamanho, i):
            array[multiplo] = 0

print("Números primos encontrados entre 2 e 999:")
for indice in range(2, tamanho):
    if array[indice] == 1:
        print(indice, end=" ")