
from utils.cores import AMARELO, VERDE, AZUL, RESET
from consumer.consumer_oracle_sql import get_empresas_por_tipo_residuo, get_nome_residuo_por_id 

def gerar_relatorio_empresas(cliente):
    print(f"\n{AZUL}🏢 ─── Gerando relatório de empresas parceiras ... ───{RESET}")
    relatorio = []
    id_residuo_cliente = cliente.get('id_residuo_aceito')
    nome_residuo_cliente = get_nome_residuo_por_id(id_residuo_cliente)

    empresas_sp_papelao = get_empresas_por_tipo_residuo(0)
    empresas_sp_plastico = get_empresas_por_tipo_residuo(1)
    empresas_sp_ambos = get_empresas_por_tipo_residuo(2)

    total_empresas_sp = len(empresas_sp_papelao) + len(empresas_sp_plastico) + len(empresas_sp_ambos)
    relatorio.append(f"Total de empresas de reciclagem cadastradas em São Paulo: {total_empresas_sp}\n")

    relatorio.append(f"Empresas que reciclam {nome_residuo_cliente if nome_residuo_cliente else 'Resíduo Desconhecido'}:\n")
    empresas_sp = get_empresas_por_tipo_residuo(id_residuo_cliente)
    if empresas_sp:
        for empresa in empresas_sp:
            relatorio.append(f"- {empresa[1]} (Localização: {empresa[2]}, Contato: {empresa[3]})\n")
    else:
        relatorio.append("Nenhuma empresa cadastrada para este tipo de resíduo.\n")

    nome_arquivo = 'relatorios.txt'
    try:
        with open(nome_arquivo, 'w') as arquivo_relatorio:
            arquivo_relatorio.writelines(relatorio)
        print(f"\n{VERDE}✅ Relatório de empresas gerado com sucesso e salvo em '{nome_arquivo}'.{RESET}")
    except IOError:
        print(f"{AMARELO}⚠️ Erro ao salvar o relatório no arquivo '{nome_arquivo}'. Verifique as permissões de escrita.{RESET}")

def gerar_relatorio(cliente_atual):
    gerar_relatorio_empresas(cliente_atual)

