#for(variavel;condição;incremento) em c funciona, python não

for i in [1,2,3,4,5,6,7,8,9,10]:
    print(i)

# ou usar o range

for i in range (0,11):
    print (i)


# se for ao contrario:
for i in range (10,0,-1):
    print (i)

lista = [i for i in range (0,11,2)]
    print(lista)