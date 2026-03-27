def verifica_parenteses(expressao):
    pilha = []

    for caractere in expressao:
        if caractere == '(':
            pilha.append('(')
        elif caractere == ')':
            if len(pilha) > 0:
                pilha.pop()
            else:
                return "Erro (fechou sem abrir)"

    if len(pilha) == 0:
        return "OK"
    else:
        return "Erro (abriu e não fechou)"