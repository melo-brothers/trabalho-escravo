import pandas as pd
from datetime import date, datetime
import httpx
import shutil

def salvar_dataframe(df: pd.DataFrame, nome_do_arquivo: str):
    nome_do_arquivo = f"{date.today()}-{nome_do_arquivo}"
    df.to_csv(f"./arquivos/processados/{nome_do_arquivo}", sep=";")
    return nome_do_arquivo


def mover_arquivo(caminho):
    origem = f"./arquivos/{caminho}"
    destino = f"./arquivos/processados/{caminho}"
    shutil.move(origem, destino)


def tratar_arquivo(caminho):
    columns = [
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

    def tratamento_de_datas(data):
        if isinstance(data, datetime):
            return data.date()
        _data = data.replace(".","").split(" ")

        for d in reversed(_data):
            try:
                d = d.split("/")
                return date(day=int(d[0]), month=int(d[1]), year=int(d[2]))
            except Exception:
                ...

    df = pd.read_excel(caminho)
    df.columns = columns

    # Procurar data no arquivo
    for linha in df.id:
        try:
            data_do_arquivo = tratamento_de_datas(linha)
        except Exception:
            ...
        else:
            break

    # Elimina os registros vazios
    # TODO: Melhorar a exclusão da lista
    df.dropna(inplace=True)


    # Resetar os índices
    df.reset_index(drop=True, inplace=True)

    # Elimina o cabeçalho do arquivo
    df.drop(0, inplace=True)


    # Tratamento de datas
    df.data_decisao_administrativa = df.data_decisao_administrativa.apply(tratamento_de_datas)
    df.data_ultima_inclusao_cadastro = df.data_inclusao_cadastro.apply(tratamento_de_datas)


    # Cria a data do arquivo
    df["data_arquivo"] = data_do_arquivo


    # Cria a data da carga
    df["data_carga"] = date.today()


    return df
