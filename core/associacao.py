# core/associacao.py

import json
from utils.cores import AMARELO, VERDE, RESET

def carregar_dados():
    """Carrega os dados do arquivo JSON."""
    try:
        with open('./data/dados.json', 'r') as arquivo:
            dados = json.load(arquivo)
            return dados.get('empresas', [])
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print(f"{AMARELO}⚠️ Erro ao decodificar o arquivo JSON. Verifique a sua estrutura.{RESET}")
        return []

def associar_residuo_empresa(tipo_residuo):
    empresas = carregar_dados()
    empresas_compatíveis = [
        empresa for empresa in empresas
        if empresa.get('tipo_residuo_aceito', '').lower() == tipo_residuo.lower()
    ]
    return empresas_compatíveis

def associacao_interativa():
    tipo = input("Digite o tipo de resíduo para buscar empresas: ")
    resultado = associar_residuo_empresa(tipo)
    if resultado:
        print(f"\n{VERDE}✅ Empresas compatíveis encontradas para '{tipo}':{RESET}")
        for empresa in resultado:
            print(f"- {empresa['nome_empresa']}")
    else:
        print(f"\n{AMARELO}❌ Nenhuma empresa compatível encontrada para '{tipo}'.{RESET}")
