from utils.cores import AMARELO, RESET, AZUL, VERDE

def solicitar_input(campo):
    while True:
        valor = input(f"{AMARELO}👉 Digite o {campo}: {RESET}").strip()
        if valor:
            return valor
        else:
            print(f"{AMARELO}⚠️  Este campo não pode estar vazio. Tente novamente.{RESET}")

def cadastrarEmpresa():
    print(f"\n{AZUL}🏢 ─── Cadastro de Empresa Parceira ───{RESET}")
    nome = solicitar_input("nome da empresa")
    ramo = solicitar_input("ramo de atuação")
    localizacao = solicitar_input("localização")
    tipo_residuo_aceito = solicitar_input("tipo de resíduo aceito (ex: embalagens, papelão)")

    empresa = {
        "nome_empresa": nome,
        "ramo_atuacao": ramo,
        "localizacao": localizacao,
        "tipo_residuo_aceito": tipo_residuo_aceito
    }

    print(f"\n{VERDE}✅ Empresa '{nome}' cadastrada com sucesso!{RESET}")
    print(empresa) # Por enquanto, apenas exibimos a empresa cadastrada
    return empresa
