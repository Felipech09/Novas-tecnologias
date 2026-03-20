palavra = input("Digite as palavras separadas com espaços: ").split()

termo = input("Digite o termo: ")

encontrado = False
for i in range(len(palavra)):
    if palavra[i] == termo:
        print("Palavra encontrada no índice:", i)
        encontrado = True
        break

if not encontrado:
    print("Palavra não encontrada.")