from leitura_arquivo import conferencia_arquivos
from processamento import tratar_arquivo, salvar_dataframe, mover_arquivo
import sys

try:
    novo_arquivo_bytes, caminho_ultimo_arquivo, nome_arquivo_novo = conferencia_arquivos()
except FileExistsError:
    print("Arquivo já processado")
    sys.exit(0)

df = tratar_arquivo(novo_arquivo_bytes)
caminho_ultimo_arquivo
salvar_dataframe(df, nome_arquivo_novo)
mover_arquivo(nome_arquivo_novo)
