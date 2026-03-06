def eh_armstrong(numero):
    texto = str(numero)
    n = len(texto)

    soma = 0
    for digito in texto:
        soma = soma + (int(digito) ** n)

    return soma == numero
    
print("--Números de Armstrong--")
inicio = int(input("Começa em:"))
fim = int(input("Termina em:"))

encontrou = False
for num in range (inicio, fim + 1):
    if eh_armstrong(num):
        print(f"O número {num} é de Armstrong")
        encontrou = True

if not encontrou:
    print("Nenhum número encontrado")
