texto = input("Digite o texto: ")
deslocamento = int(input("Digite o deslocamento: "))

resultado = ""

for c in texto:
    if 'a' <= c <= 'z':
        nova = (ord(c) - ord('a') + deslocamento) % 26 + ord('a')
        resultado += chr(nova)

    elif 'A' <= c <= 'Z':
        nova = (ord(c) - ord('A') + deslocamento) % 26 + ord('A')
        resultado += chr(nova)

print("Texto cifrado:", resultado)