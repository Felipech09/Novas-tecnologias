# dicionario={'101':'Joao'} 
# conj={1,2,3}

dicionario={'nome':'joao', 'idade':'20'} # chave(nome e idade):valor(joao e 20) sempre assim
dicionario['idade'] = 22 # alterar o valor
# CHAVE SEMPRE INDICADA COMO STRING, OU SEJA ENTRE ''
print(dicionario)
dicionario = dict(nome='joao', idade=20)
#CHAVE NÃO SE ALTERA, NUNCA, apenas cria e deleta
del dicionario ['nome'] # pra remover uma chave
print(dicionario)

lista = [1,1,2,2,3,3,4,4,5,5,6,7,7,8]
dicionario = {}
for i in lista:
    dicionario[i] = dicionario.get(i,0)+1

for num, qtd in dicionario.itens():
    if qtd >= 3:
        print(num)
