# Função auxiliar para forçar entrada válida
def solicitar_input(campo):
    while True:
        valor = input(f"{campo}").strip()
        if valor:
            return valor
        else:
            print(f"⚠️  Este campo não pode estar vazio. Tente novamente.")

def cadastrarEmpresa():
    nome = solicitar_input("Digite o nome da empresa: ")
    ramo = solicitar_input("Digite o ramo de atuação: ")
    localizacao = solicitar_input("Digite a localização: ")
    produto = solicitar_input("Digite o produto fabricado: ")
    
    empresa = { "nome_empresa": nome,
                "ramo_atuacao": ramo,
                "localizacao": localizacao,
                "produto": produto}
    
    # print(f"Empresa {nome} cadastrada com sucesso!")

    return empresa


# print(cadastrarEmpresa())
