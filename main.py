from core import clientes, associacao, relatorios
from utils.cores import AMARELO, VERDE, AZUL, RESET

def menu_principal():
    try:
        while True:
            print(f"""
                    {AZUL}=== SISTEMA DE GESTÃO DE RESÍDUOS ==={VERDE}
                    1. Cadastrar Cliente
                    0. Sair
                    """
                )
            opcao = input(f"{AMARELO}Escolha uma opção: {RESET}")

            if opcao == '1':
                cliente = clientes.cadastrar_cliente()
                if cliente:
                    menu_cliente(cliente)
            elif opcao == '0':
                print(f"{VERDE}Saindo do sistema principal...{RESET}")
                break
            else:
                print(f"{AMARELO}Opção inválida. Tente novamente no menu principal.{RESET}")

    except KeyboardInterrupt:
        print("\nEncerrando o programa. Até logo!")

def menu_cliente(cliente):
    try:
        while True:
            print(f"""
                    {AZUL}=== Menu Cliente: {cliente['nome_empresa']} ==={VERDE}
                    1. Associar resíduo a empresa parceira
                    2. Gerar relatório
                    0. Sair do menu do cliente
                    """
                )
            opcao = input(f"{AMARELO}Escolha uma opção: {RESET}")

            if opcao == '1':
                associacao.associacao_interativa(cliente)
            elif opcao == '2':
                relatorios.gerar_relatorio(cliente)
            elif opcao == '0':
                print(f"{VERDE}Saindo do menu do cliente...{RESET}")
                break
            else:
                print(f"{AMARELO}Opção inválida. Tente novamente no menu do cliente.{RESET}")

    except KeyboardInterrupt:
        print("\nEncerrando o menu do cliente.")

if __name__ == "__main__":
    menu_principal()