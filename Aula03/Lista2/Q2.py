import math

hora = int(input("Digite a hora: "))
chuva = int(input("Digite 1 para chuva e 0 pra sem chuva: "))
fluxo = int(input("Digite o fluxo: 0 baixo, 1 médio, 2 alto: "))

if (7 <= hora <= 9) or (17 <= hora <= 19):
    tempo = 60
else:
    tempo = 35

if chuva == 1:
    tempo *= 1.2

if fluxo == 2:
    tempo += 15
elif fluxo == 0:
    tempo -= 10
else: 
    tempo

print("O tempo final é: ", tempo)