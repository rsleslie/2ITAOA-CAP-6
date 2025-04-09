import cx_Oracle
from config.database_config import ORACLE_USERNAME, ORACLE_PASSWORD, ORACLE_DSN

def conectar():
    connection = cx_Oracle.connect(
        user=ORACLE_USERNAME,
        password=ORACLE_PASSWORD,
        dsn=ORACLE_DSN
    )
    return connection
