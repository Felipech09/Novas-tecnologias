str=input("Digite um número: " )
base=int (input("Escolha a base (8, 10 ou 16)"))

numero_int = int(str, base)

print("Valor em decimal:", numero_int)
print("Valor em hexadecimal:", hex(numero_int))
print("Valor em octal:", oct(numero_int))