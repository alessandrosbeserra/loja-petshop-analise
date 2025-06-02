import mysql.connector
import pandas as pd

# 🔒 Configuração da conexão
config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'loja_petshop',
    'port': 3306
}

# Conectar ao MySQL
conexao = mysql.connector.connect(**config)
cursor = conexao.cursor()

# Obter lista de tabelas
cursor.execute("SHOW TABLES;")
tabelas = [linha[0] for linha in cursor.fetchall()]

# Exportar cada tabela para CSV
for tabela in tabelas:
    print(f"Exportando tabela: {tabela}")
    df = pd.read_sql(f"SELECT * FROM {tabela};", conexao)
    df.to_csv(f"{tabela}.csv", index=False)

# Fechar conexão
cursor.close()
conexao.close()
print("Exportação finalizada.")
