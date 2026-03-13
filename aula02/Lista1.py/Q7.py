frase = input("Digite uma frase: ")

frase_minuscula = frase.lower()

vogais = "aeiou"

contador = 0

for letra in frase_minuscula:
    if letra in vogais:
        contador += 1

print("Quantidade de vogais na frase:", contador)