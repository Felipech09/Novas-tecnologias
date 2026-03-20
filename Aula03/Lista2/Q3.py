def anagrama(frase1, frase2):
    f1 = frase1.replace(" ", "").lower()
    f2 = frase2.replace(" ", "").lower()
    
    return sorted(f1) == sorted(f2)

p1 = input("Digite a primeira palavra: ")
p2 = input("Digite a segunda palavra: ")

if anagrama(p1, p2):
    print("São anagramas")
else:
    print("Não são anagramas")
