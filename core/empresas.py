def cadastrarEmpresa():
    nome = input("Digite o nome da empresa: ")
    ramo = input("Digite o ramo de atuação: ")
    localizacao = input("Digite a localização: ")
    produto = input("Digite o produto fabricado: ")
    
    empresa = { "nome_empresa": nome,
                "ramo_atuacao": ramo,
                "localizacao": localizacao,
                "produto": produto}
    
    print(f"Empresa {nome} cadastrada com sucesso!")

    return empresa


# print(cadastrarEmpresa())
