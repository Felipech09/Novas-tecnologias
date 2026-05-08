import sys #manipulação de linhas de comando via prompt
file = open ('teste.txt', 'w')

texto = "Lorem ipsum is a dummy or placeholder text commonly used in graphic design, publishing, and web development to fill space in layouts without distracting from the design itself. The text is a corrupted version of Cicero's 1st-century BC work, De Finibus Bonorum et Malorum, with words altered, added, or removed to make it nonsensical Latin. The first word, orem, is a truncation of dolorem, which means pain in Latin, but in the context of the placeholder text, it has no actual meaning"

file.write(texto)

file.close