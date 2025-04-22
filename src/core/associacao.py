from utils.cores import AMARELO, VERDE, AZUL, RESET
from consumer.consumer_oracle_sql import get_nome_residuo_por_id, get_empresas_por_tipo_residuo

def listar_empresas_coleta(id_residuo, localizacao):
    empresas_db = get_empresas_por_tipo_residuo(id_residuo)

    return empresas_db

def get_nome_residuo(id_residuo):
    residuo = get_nome_residuo_por_id(id_residuo)
    return residuo

def associacao_interativa(cliente):
    id_residuo_cliente = cliente.get('id_residuo_aceito')
    localizacao_cliente = cliente.get('localizacao', '').lower()
    nome_residuo = get_nome_residuo_por_id(id_residuo_cliente)

    if id_residuo_cliente is None:
        print(f"{AMARELO}⚠️ O tipo de resíduo aceito pelo cliente não está definido.{RESET}")
        return

    print(f"\n{AZUL}🤝 ─── Empresas de Coleta para '{nome_residuo}' em '{localizacao_cliente.capitalize()}' ───{RESET}")
    empresas_encontradas = listar_empresas_coleta(id_residuo_cliente, localizacao_cliente)
    
    nome_residuo_cliente = get_nome_residuo(id_residuo_cliente)
  
    print(f"{VERDE}✅ Empresas de coleta seletiva encontradas na sua região:{RESET}")
    print("-" * 80)
    print(f"{'Empresa':<30} {'Resíduo':<15} {'Localização':<20} {'Contato':<20}")
    print("-" * 80)
    for empresa in empresas_encontradas:
        print(f"{empresa[1]:<30} {nome_residuo_cliente:<15} {empresa[2]:<20} {empresa[3]:<20}")
    print("-" * 80)
        
   


    

