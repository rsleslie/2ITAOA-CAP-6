from utils.cores import AZUL,VERDE,AMARELO,RESET
from core.empresas import cadastrarEmpresa
from utils.validacoes import validar_dados

def main():

    try:
        while True:
            print(f"\n{AZUL}📋 ─── MENU ───{RESET}")
            print(f"{VERDE}1️⃣  Cadastrar nova empresa{RESET}")
            print(f"{VERDE}2️⃣  Listar empresas{RESET}")
            print(f"{VERDE}3️⃣  🚪 Sair{RESET}")

            opcao = input(f"\n{AMARELO}👉 Escolha uma opção: {RESET}")
            print("\n")
            if opcao == "1":
                validar_dados(cadastrarEmpresa())
            elif opcao == "2":
                # listar_empresas()
                print("Ainda não Implementei **so uma ideia")
            elif opcao == "3":
                print("Saindo... Até logo!")
                break
            else:
                print("Opção inválida.")

    except KeyboardInterrupt:
        print("\nEncerrando o programa. Até logo!")


if __name__ == "__main__":
    main()


