x=4

if x>5:
    print("Maior")
else:
    print("Menor")

while True:
    menu=int(input (
    """
            ***************
            **calculadora**
            *1-soma       *
            *2-subtração  *
            *3-divisão    *
            *4-produto    *
            *5-smultiplos *
            *6-sair       *
            ***************
    """
))

#    if menu == 1:
#        print("soma")
#    elif menu == 2:
#        print("Subtração")
#    elif menu == 3:
#        print("Divisão")
#    elif menu == 4:
#        print("Produto")
#    else:
#        print("Seleção errada")

# para fazer o famoso switch case em python se usa o match

    x = float(input("DIgite um número: "))
    y = float(input("DIgite um número: "))

    match menu:
        case 1:
            print("soma")
        case 2:
            print("Subtração")
        case 3:
            print("Não existe divisão por zero") if y==0 else print("Divisão") # a sintaxe do python é assim
        case 4:
            print("Produto")
        case 5: 
            for i in range(1,int(y)):
                print(x*i)
        case 6:
            break
        case _:
            print("Seleção errada")