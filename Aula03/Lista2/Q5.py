a = int(input("Digite o valor A: "))
b = int(input("Digite o valor B: "))
p = int(input("Digite o peso: "))

if p == 0:
    print("Erro, o peso não pode ser zero")
elif a < b and p <= 0:
    print("Erro: passo deve ser positivo quando a < b.")
elif a > b and p >= 0:
    print("Erro: passo deve ser negativo quando a > b.")
else:
    cont = 0
    if a < b:
        for i in range(a, b+1, p):
            print(i)
            cont += 1
    else:
        for i in range(a, b-1, p):
            print(i)
            cont += 1
    print("Quantidade de valores impressos:", cont)