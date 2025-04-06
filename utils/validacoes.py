from utils.cores import AMARELO

def validar_localizacao(dicionario):
    localizacoes_aceitas = ["São Paulo"]

    if "localizacao" not in dicionario or not dicionario["localizacao"].strip():
        print("Localização não informada")
        return False
    elif dicionario["localizacao"] in localizacoes_aceitas:
        return True
    else:
        print(f"\n{AMARELO}Não atendemos essa área 😢")
        return False


def validar_produto(dicionario):
    produtos_aceitos = ["papelao"]

    if "produto" not in dicionario or not dicionario["produto"].strip():
        print("Produto não informado.")
        return False
    elif dicionario["produto"] in produtos_aceitos:
        return True
    else:
        print("Não atendemos esse produto")
        return False


def validar_dados(empresa):

    if validar_localizacao(empresa) and validar_produto(empresa):
        print(f"\n\n✅  Empresa {empresa["nome_empresa"]} cadastrada com sucesso!")
        return empresa
    else:
        return []