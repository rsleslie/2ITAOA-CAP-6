from utils.cores import  AMARELO, VERDE, RESET, AZUL

def solicitar_input(campo):
    while True:
        valor = input(f"{AMARELO}👉 Digite o {campo}: {RESET}").strip()
        if valor:
            return valor
        else:
            print(f"{AMARELO}⚠️  Este campo não pode estar vazio. Tente novamente.{RESET}")

def solicitar_quantidade():
    while True:
        quantidade_str = input(f"{AMARELO}👉 Digite a quantidade: {RESET}").strip()
        if quantidade_str.isdigit():
            return int(quantidade_str)
        else:
            print(f"{AMARELO}⚠️  Por favor, digite um número válido para a quantidade.{RESET}")

def solicitar_destinacao():
    print(f"{VERDE}Opções de Destinação:{RESET}")
    print(f"{VERDE}1 - Reciclagem{RESET}")
    print(f"{VERDE}2 - Compostagem{RESET}")
    print(f"{VERDE}3 - Incineração{RESET}")
    print(f"{VERDE}4 - Outro{RESET}")
    while True:
        opcao = input(f"{AMARELO}👉 Escolha a destinação (1-4): {RESET}").strip()
        if opcao in ["1", "2", "3", "4"]:
            if opcao == "4":
                return solicitar_input("outra destinação")
            elif opcao == "1":
                return "Reciclagem"
            elif opcao == "2":
                return "Compostagem"
            elif opcao == "3":
                return "Incineração"
        else:
            print(f"{AMARELO}⚠️  Opção inválida. Escolha entre 1 e 4.{RESET}")

def cadastrar_residuo():
    print(f"\n{AZUL}📝 ─── Cadastro de Resíduo ───{RESET}")
    tipo = solicitar_input("tipo de resíduo (embalagem, restos de safra, etc)")
    quantidade = solicitar_quantidade()
    data_descarte = solicitar_input("data do descarte (DD/MM/AAAA)")

    # Aqui podemos adicionar a validação da data no futuro
    destinacao = solicitar_destinacao()

    residuo = {
        "tipo": tipo,
        "quantidade": quantidade,
        "data_descarte": data_descarte,
        "destinacao": destinacao
    }

    print(f"\n{VERDE}✅ Resíduo cadastrado com sucesso!{RESET}")
    print(residuo) # Por enquanto, apenas exibimos o resíduo cadastrado
    return residuo