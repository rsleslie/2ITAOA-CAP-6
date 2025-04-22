from utils.cores import AMARELO, RESET, AZUL, VERDE
from core.armazenamento import carregar_dados, salvar_dados
from consumer.consumer_oracle_sql import get_nome_residuo_por_id

def solicitar_input(campo):
    while True:
        valor = input(f"{AMARELO}👉 Digite o {campo}: {RESET}").strip()
        if valor:
            return valor
        else:
            print(f"{AMARELO}⚠️  Este campo não pode estar vazio. Tente novamente.{RESET}")

def escolher_tipo_residuo():
    while True:
        print(f"{AMARELO}Escolha o tipo de resíduo aceito:{RESET}")
        print(f"{VERDE}0 - Papelão{RESET}")
        print(f"{VERDE}1 - Plástico{RESET}")
        opcao = input(f"{AMARELO}👉 Digite a opção (0 ou 1): {RESET}").strip()
        if opcao == '0':
            return 0
        elif opcao == '1':
            return 1
        else:
            print(f"{AMARELO}⚠️ Opção inválida. Escolha 0 para Papelão ou 1 para Plástico.{RESET}")

def escolher_localizacao():
    while True:
        print(f"{AMARELO}Escolha a localização:{RESET}")
        print(f"{VERDE}1 - São Paulo{RESET}")
        print(f"{VERDE}2 - Outra cidade (Não atendemos){RESET}")
        opcao = input(f"{AMARELO}👉 Digite a opção (1 ou 2): {RESET}").strip()
        if opcao == '1':
            return "sao paulo"
        elif opcao == '2':
            print(f"{AMARELO}⚠️ Desculpe, ainda não atendemos em outras cidades.{RESET}")
            return None
        else:
            print(f"{AMARELO}⚠️ Opção inválida. Escolha 1 para São Paulo ou 2 para outras cidades.{RESET}")

            
def cadastrar_cliente():
    print(f"\n{AZUL}🏢 ─── Cadastro de Cliente ───{RESET}")
    nome_empresa = solicitar_input("nome da empresa")
    ramo_atuacao = solicitar_input("ramo de atuação")
    localizacao = escolher_localizacao()
    if localizacao is None:
        return None
    id_residuo_aceito = escolher_tipo_residuo()

    cliente = {
        "nome_empresa": nome_empresa,
        "ramo_atuacao": ramo_atuacao,
        "localizacao": localizacao,
        "id_residuo_aceito": id_residuo_aceito
    }
  
    dados = carregar_dados()
    dados.setdefault('clientes', []).append(cliente)
    salvar_dados(clientes=dados.get('clientes'))
    print(f"\n{VERDE}✅ Cliente '{nome_empresa}' cadastrado com sucesso! Resíduo: {get_nome_residuo_por_id(id_residuo_aceito)}{RESET}")
    return cliente
