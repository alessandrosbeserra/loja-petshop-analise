
import mysql.connector
import pandas as pd

# Configurações de conexão
config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'loja_petshop',
    'port': 3306
}

# 📡 Conectar ao banco
conexao = mysql.connector.connect(**config)

# Função para executar uma consulta e retornar DataFrame
def consultar_view(view_name):
    query = f"SELECT * FROM {view_name};"
    df = pd.read_sql(query, conexao)
    return df

# 🔁 Views a consultar
views = [
    'vw_vendas_por_mes',
    'vw_produtos_mais_vendidos',
    'vw_clientes_top',
    'vw_faturamento_por_categoria',
    'vw_estoque_baixo',
    'vw_pedidos_detalhados'
]

# 📂 Extrair e salvar resultados
for view in views:
    df = consultar_view(view)
    print(f"\n=== {view} ===")
    print(df.head())
    df.to_csv(f'{view}.csv', index=False)

# ✅ Fechar conexão
conexao.close()
