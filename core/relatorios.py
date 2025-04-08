from database.db import conectar
from utils.cores import AMARELO, VERDE

def obter_materiais_disponiveis():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT tipo_material FROM empresas_parceiras")
    materiais = [row[0] for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return materiais

def exibir_opcoes_materiais(materiais):
    print(f"{VERDE}🔎 Tipos de materiais disponíveis:{AMARELO}")
    for i, mat in enumerate(materiais, 1):
        print(f"{i} - {mat}")
    print()

def escolher_material(materiais):
    try:
        escolha = int(input("👉 Escolha um número: ")) - 1
        return materiais[escolha]
    except (ValueError, IndexError):
        print("❌ Opção inválida.")
        return None

def solicitar_localizacao():
    return input("📍 Digite a localização: ").strip()

def buscar_empresas_por_material(material):
    conn = conectar()
    cursor = conn.cursor()
    sql = """
        SELECT * FROM empresas_parceiras
        WHERE tipo_material = :material
    """

    cursor.execute(sql, material=material)
    resultados = cursor.fetchall()
    cursor.close()
    conn.close()
    return resultados

def exibir_empresas(resultados):
    if resultados:
        print(f"\n{VERDE}✅ Empresas compatíveis encontradas:")
        for empresa in resultados:
            print(f"🏢 Empresa: {empresa[1]} | 📞 Contato: {empresa[4]}")
    else:
        print("❌ Nenhuma empresa parceira disponível para essa coleta.")

def buscar_empresa_compativel_interativo():
    materiais = obter_materiais_disponiveis()
    if not materiais:
        print("⚠️ Nenhum material encontrado no banco.")
        return

    exibir_opcoes_materiais(materiais)
    tipo_material = escolher_material(materiais)
    if not tipo_material:
        return

    resultados = buscar_empresas_por_material(tipo_material)
    exibir_empresas(resultados)
