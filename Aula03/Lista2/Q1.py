import re

palavra = input("Digite uma palavra: ")

invertida = ""

def palindromo(texto):
    texto_normal = re.sub(r'[^a-zA-Z]', '', texto)
    texto_normal = texto_normal.lower()

for i in range( len(palavra)-1, -1, -1):
    invertida += palavra[i]

print(palavra,invertida)

if palavra == invertida:
    print("É palindromo")
else:
    print("não é palindromo")