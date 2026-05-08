import os #mexe com diretórios(pastas)

print(os.getcwd())          # Mostra o diretório atual
print(os.listdir())         # Lista arquivos e pastas
os.mkdir("testando")        # Cria um diretório
os.rename("testando", "teste")  # Renomeia o diretório
os.rmdir("teste")           # Remove o diretório