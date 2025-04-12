from database.db import conectar

def get_empresas_por_tipo_residuo(tipo_residuo_id):

    conn = None
    cursor = None
    resultados = []
    try:
        conn = conectar()
        cursor = conn.cursor()
        sql = """
            SELECT id_empresa, nome, localizacao, contato
            FROM empresas_parceiras
            WHERE id_residuo = :residuo_id OR id_residuo = 2
        """
        cursor.execute(sql, residuo_id=tipo_residuo_id)
        resultados = cursor.fetchall()
    except Exception as e:
        print(f"Erro ao consultar a tabela 'empresas_parceiras': {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
    return resultados

def get_nome_residuo_por_id(residuo_id):

    conn = None
    cursor = None
    nome_residuo = None
    try:
        conn = conectar()
        cursor = conn.cursor()
        sql = """
            SELECT nome_residuo FROM tipos_residuo
            WHERE id_residuo = :id
        """
        cursor.execute(sql, id=residuo_id)
        resultado = cursor.fetchone()
        if resultado:
            nome_residuo = resultado[0]
    except Exception as e:
        print(f"Erro ao consultar a tabela 'tipos_residuo': {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
    return nome_residuo
