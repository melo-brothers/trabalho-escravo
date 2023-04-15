
# Faz o request na página -> https://www.gov.br/trabalho-e-previdencia/pt-br/composicao/orgaos-especificos/secretaria-de-trabalho/inspecao/areas-de-atuacao/combate-ao-trabalho-escravo-e-analogo-ao-de-escravo
# Encontro o arquivo XLSX
# Baixo o arquivo XLSX
# Comparo o arquivo baixado com o único arquivo na pasta arquivos. Se o arquivo for igual (HASH), interrompe. Se o arquivo for diferente, continua o processamento
# Move o arquivo que já estava na pasta "arquivos" para "processados"
# Salva o novo arquivo na pasta arquivos
# Schedular a execução (Rocketry)
# Logging

import httpx
import re
from datetime import date
import os
import shutil
import hashlib
from processamento import tratar_arquivo

PAGINA_GOV = "https://www.gov.br/trabalho-e-previdencia/pt-br/composicao/orgaos-especificos/secretaria-de-trabalho/inspecao/areas-de-atuacao/combate-ao-trabalho-escravo-e-analogo-ao-de-escravo"
PADRAO = 'https://www.gov.br/trabalho-e-previdencia/pt-br/composicao/orgaos-especificos/secretaria-de-trabalho/inspecao/areas-de-atuacao/.*xlsx"'


# TODO: Salvar o aquivo com a data que está dentro do dataframe
# TODO: Terminar esta função de salvar arquivo
def salvar_novo_arquivo(nome_arquivo_antigo, bytes, nome_do_arquivo_novo: str):
    nome_do_arquivo_novo = f"{date.today()}-{nome_do_arquivo_novo}"

    with open(f"./arquivos/{nome_do_arquivo_novo}", "wb+") as f:
        f.write(bytes)

    origem = f"./arquivos/{nome_arquivo_antigo}"
    destino = f"./arquivos/brutos/{nome_arquivo_antigo}"
    shutil.move(origem, destino)


def conferencia_arquivos():

    def compare_files(arq1, arq2):
        hash_1 = hashlib.new('ripemd160')
        hash_1.update(open(arq1, 'rb').read())
        hash_2 = hashlib.new('ripemd160')
        hash_2.update(arq2)

        return hash_1.digest() == hash_2.digest()

    def encontra_link_planilha(padrao, pagina):
        match = re.search(padrao, pagina.text)
        result = match.group(0)[:-1]
        nome_temporario = result.split("/")[-1]
        return result, nome_temporario

    # Carrega a página de trabalho escravo
    pagina = httpx.get(PAGINA_GOV)
    url_arquivo, nome_temporario = encontra_link_planilha(PADRAO, pagina)

    for (_,_,files) in os.walk('./arquivos'):
        arquivo_existente = files[0]
        caminho_ultimo_arquivo = f'./arquivos/{files[0]}'
        break

    arquivo_temporario = httpx.get(url_arquivo)

    # Verifica se o arquivo é igual ao existente
    if compare_files(caminho_ultimo_arquivo, arquivo_temporario.content):
        raise FileExistsError()

    return arquivo_temporario.content, caminho_ultimo_arquivo, nome_temporario, arquivo_existente
