import mysql.connector
import pandas as pd

#  Configurações de conexão
config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'loja_petshop',
    'port': 3306
}

# Conectando ao Banco de dados
conexao = mysql.connector.connect(**config)

# função para executar uma consulta e retorna DataFrame
def consultar_view(view_name):
    query = f"SELECT * FROM {view_name};"
    df = pd.read_sql(query,conexao)
    return df

views = [
    'vw_vendas_por_mes',
    'vw_produtos_mais_vendidos',
    'vw_clientes_top',
    'vw_faturamento_por_categoria',
    'vw_estoque_baixo',
    'vw_pedidos_detalhados'
]

df_exemplo = consultar_view(views[0])
print(df_exemplo)

resultados = {}

for view in views:
    resultados[view] = consultar_view(view)

print(resultados['vw_clientes_top'])


# Fecha conexão
conexao.close()