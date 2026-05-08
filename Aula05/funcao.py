print.__doc__ # olhar documentação da função

def soma(a,b):
    return a+b

soma(2,3)

def saudacao():
    print("olá mundo")


def intervalo (a,b,p=1):
    for x in range(a,b,p):
        print(x)

intervalo = (2,8,2)
intervalo = (2,8)
intervalo(p=2,a=2,b=8)

mais = lambda a,b:a+b # outra forma de fazer só que usando uma linha só

def calculadora(a,b):
    return a+b, a*b, a-b, a/b
calculadora(10,2)
print(calculadora)