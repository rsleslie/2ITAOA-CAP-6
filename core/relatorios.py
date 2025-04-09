import json
from utils.cores import AMARELO, VERDE, AZUL, RESET

def carregar_dados_residuos():
    """Carrega os dados de resíduos do arquivo JSON."""
    try:
        with open('./data/dados.json', 'r') as arquivo:
            dados = json.load(arquivo)
            return dados.get('residuos', [])
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print(f"{AMARELO}⚠️ Erro ao decodificar o arquivo JSON de resíduos. Verifique a sua estrutura.{RESET}")
        return []

def gerar_relatorio_total_residuos():
    """Gera um relatório com o total de resíduos por tipo."""
    print(f"\n{AZUL}📊 ─── Relatório: Total de Resíduos por Tipo ───{RESET}")
    residuos = carregar_dados_residuos()
    total_por_tipo = {}

    if not residuos:
        print(f"{AMARELO}⚠️ Nenhum resíduo cadastrado ainda.{RESET}")
        return

    for residuo in residuos:
        tipo = residuo.get('tipo')
        quantidade = residuo.get('quantidade', 0)
        if tipo:
            total_por_tipo[tipo] = total_por_tipo.get(tipo, 0) + quantidade

    if total_por_tipo:
        for tipo, total in total_por_tipo.items():
            print(f"{VERDE}➡️ Tipo: {tipo} - Total: {total}{RESET}")
    else:
        print(f"{AMARELO}⚠️ Nenhum resíduo encontrado para gerar o relatório.{RESET}")


def gerar_relatorio():
    gerar_relatorio_total_residuos()