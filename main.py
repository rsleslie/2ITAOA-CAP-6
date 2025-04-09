from core import residuos, empresas, associacao, relatorios
from utils.cores import AMARELO, VERDE, AZUL, RESET

def menu_principal():
    try:
        while True:
            print(f"""
                    {AZUL}=== SISTEMA DE GESTÃO DE RESÍDUOS ==={VERDE}
                    1. Cadastrar resíduo
                    2. Cadastrar Cliente
                    3. Associar resíduo a empresa parceira
                    4. Gerar relatório
                    0. Sair
                    """
                )
            opcao = input(f"{AMARELO}Escolha uma opção: {RESET}")

            if opcao == '1':
                residuos.cadastrar_residuo()
            elif opcao == '2':
                empresas.cadastrarEmpresa()
            elif opcao == '3':
                associacao.associacao_interativa()
            elif opcao == '4':
                relatorios.gerar_relatorio()
            elif opcao == '0':
                print(f"{VERDE}Saindo do sistema...{RESET}")
                break
            else:
                print(f"{AMARELO}Opção inválida. Tente novamente.{RESET}")

    except KeyboardInterrupt:
        print("\nEncerrando o programa. Até logo!")

if __name__ == "__main__":
    menu_principal()