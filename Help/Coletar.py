import os

# Diretório onde as imagens estão localizadas
diretorio_imagens = "C:/Users/User/OneDrive/Área de Trabalho/Arquivos/Python/War robots automat/War robots automation/imgs"

# Lista de extensões de imagem suportadas
extensoes_imagem = [".png", ".jpg", ".jpeg", ".gif"]

# Lista para armazenar os nomes de imagens formatados
nomes_imagens = []

# Listar os arquivos no diretório
arquivos_no_diretorio = os.listdir(diretorio_imagens)
print(arquivos_no_diretorio)

# Filtrar apenas os arquivos de imagem
for arquivo in arquivos_no_diretorio:
    nome, extensao = os.path.splitext(arquivo)
    if extensao.lower() in extensoes_imagem:
        nome_formatado = f'"{nome.replace("_", " ").title()}{extensao}",'
        nomes_imagens.append(nome_formatado)

# Juntar os nomes de imagens formatados em uma única string
nomes_imagens_str = "\n".join(nomes_imagens)

# Copiar a string para a área de transferência
import pyperclip
pyperclip.copy(nomes_imagens_str)

print("Nomes de imagens formatados copiados para a área de transferência.")
