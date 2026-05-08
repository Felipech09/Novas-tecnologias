import zipfile # faz arquivos zip

texto = "Lorem ipsum is a dummy or placeholder text commonly used in graphic design, publishing, and web development to fill space in layouts without distracting from the design itself. The text is a corrupted version of Cicero's 1st-century BC work, De Finibus Bonorum et Malorum, with words altered, added, or removed to make it nonsensical Latin. The first word, orem, is a truncation of dolorem, which means pain in Latin, but in the context of the placeholder text, it has no actual meaning"

# Cria um zip novo
zip = zipfile.ZipFile('teste.zip', 'w', zipfile.ZIP_DEFLATED)

# Escreve uma string no zip como se fosse um arquivo
zip.writestr('texto.txt', texto)

# Fecha o zip
zip.close()

