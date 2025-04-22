import json
from utils.cores import AMARELO, VERDE, RESET
import os

ARQUIVO_DADOS = './data/dados.json'

def carregar_dados():
    """Carrega os dados do arquivo JSON."""
    if not os.path.exists(ARQUIVO_DADOS):
        return {}
    try:
        with open(ARQUIVO_DADOS, 'r') as arquivo:
            dados = json.load(arquivo)
            return dados
    except json.JSONDecodeError:
        print(f"{AMARELO}⚠️ Erro ao decodificar o arquivo JSON. O arquivo pode estar vazio ou corrompido. Criando um novo.{RESET}")
        return {}

def salvar_dados(residuos=None, clientes=None):
    """Salva os dados de resíduos e/ou clientes no arquivo JSON."""
    dados = carregar_dados()
    if residuos is not None:
        dados['residuos'] = residuos
    if clientes is not None:
        dados['clientes'] = clientes

    try:
        with open(ARQUIVO_DADOS, 'w') as arquivo:
            json.dump(dados, arquivo, indent=4)
        print(f"{VERDE}💾 Dados salvos com sucesso em '{ARQUIVO_DADOS}'.{RESET}")
    except IOError:
        print(f"{AMARELO}⚠️ Erro ao salvar os dados no arquivo '{ARQUIVO_DADOS}'. Verifique as permissões de escrita.{RESET}")

