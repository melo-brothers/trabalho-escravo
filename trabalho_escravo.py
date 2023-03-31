# Baixar o arquivo (TXT)
# Verifica se o arquivo já foi processado
# Carrega o arquivo
# Processa o arquivo
from pydantic import BaseModel, validator
from datetime import date, datetime

# TODO: Validar cada linha se inicia com um número (isso é uma linha válida!)

CAMPOS =[
    "id",
    "ano_acao_fiscal",
    "uf",
    "empregador",
    "cpf_cpnj",
    "estabelecimento",
    "trabalhadores_envolvidos",
    "cnae",
    "data_decisao_administrativa",
    "data_inclusao_cadastro",
]

class Registro(BaseModel):
    id: int
    ano_acao_fiscal: int
    uf: str
    empregador: str
    cpf_cpnj: str
    estabelecimento: str
    trabalhadores_envolvidos: int
    cnae: str
    data_decisao_administrativa: date
    data_inclusao_cadastro: date
    data_da_carga: date = date.today()

    @validator("data_decisao_administrativa", pre=True)
    def parse_data_decisao_administrativa(cls, value):
        return datetime.strptime(
            value,
            "%d/%m/%Y"
        ).date()

    @validator("data_inclusao_cadastro", pre=True)
    def parse_data_inclusao_cadastro(cls, value):
        return datetime.strptime(
            value,
            "%d/%m/%Y"
        ).date()


def leitura_arquivo():
    """ Verifica se existe um arquivo não processado na
        pasta arquivos e faz a leitura
    """
    with open("./arquivos/cadastro_de_empregadores-atualizacao-extraord-09-mar-2023.txt", "r") as f:
        return f.readlines()


def limpar_registro(linha: str) -> list[str]:
    return linha.strip().split("\t")


def empacota_registro(linha: list) -> dict:
    itens = zip(CAMPOS, linha)
    d = {}
    for c, v in itens:
        d[c] = v
    return d


def registrar_empregadores(arquivo: list) -> list[Registro]:
    """Cria uma lista e adiciona todos os empregadores válido a ela"""
    resposta = []

    for a in arquivo:
        _linha = limpar_registro(a)
        _linha = empacota_registro(_linha)
        try:
            resposta.append(Registro(**_linha))
        except Exception as e:
            ...
    return resposta


def main():
    arquivo = leitura_arquivo()
    lista_empregadores = registrar_empregadores(arquivo=arquivo)
    print(len(lista_empregadores))


if __name__ == "__main__":
    main()
