from trabalho_escravo import (
    leitura_arquivo,
    registrar_empregadores,
    limpar_registro,
    empacota_registro,
    Registro,
)


def test_leitura_arquivo():
    assert leitura_arquivo


def test_empacota_registro():
    assert empacota_registro


def test_registrar_empregadores():
    assert registrar_empregadores


def test_limpar_registro():
    assert limpar_registro


def test_limpar_registro_transforma_string_em_lista_valida():
    entrada = "33	2019	PA	Carlos Gonçalves Guimarães	483.178.292-00	Fazenda Bom Jesus, Rio Jarauçu, zona rural, Medicilândia/PA	8	1512-0/01	23/02/2021	05/04/2021																																																																																						"
    expectativa = [
        "33",
        "2019",
        "PA",
        "Carlos Gonçalves Guimarães",
        "483.178.292-00",
        "Fazenda Bom Jesus, Rio Jarauçu, zona rural, Medicilândia/PA",
        "8",
        "1512-0/01",
        "23/02/2021",
        "05/04/2021",
    ]
    assert limpar_registro(entrada) == expectativa


def test_classe_registro():
    assert Registro


def test_criar_registro_valido():
    registro = Registro(
        id=1,
        ano_acao_fiscal=2020,
        uf="PI",
        empregador="FULANO DE TAL",
        cpf_cpnj="000.000.002-72",
        estabelecimento="Cerâmica J.A, Rodovia PI, sentido de Barras a Cabaceiras",
        trabalhadores_envolvidos=2233,
        cnae="2342-7/02",
        data_decisao_administrativa="22/01/2020",
        data_inclusao_cadastro="05/04/2022",
    )
    assert registro


def test_cria_registro_a_partir_da_lista():
    linha = [
        "170",
        "2020",
        "MS",
        "Vilceu Roberto Pivetta",
        "016.101.279-51",
        "Fazenda LH, Rua das Avencas, 261 e Rua Das Flores, 832, Itaquiraí/MS",
        "24",
        "0119-9/06",
        "14/05/2021",
        "05/10/2021",
    ]
    print(*linha)
    assert Registro(
        id="170",
        ano_acao_fiscal="2020",
        uf="MS",
        empregador="Vilceu Roberto Pivetta",
        cpf_cpnj="016.101.279-51",
        estabelecimento="Fazenda LH, Rua das Avencas, 261 e Rua Das Flores, 832, Itaquiraí/MS",
        trabalhadores_envolvidos="24",
        cnae="0119-9/06",
        data_decisao_administrativa="14/05/2021",
        data_inclusao_cadastro="05/10/2021",
    )
