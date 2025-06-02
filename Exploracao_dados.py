import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Ajustes visuais
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

# =================== 1. Carregar os dados tratados ===================
clientes = pd.read_csv("clientes_tratados.csv")
produtos = pd.read_csv("produtos_tratados.csv")
pedidos = pd.read_csv("pedidos_tratados.csv")
itens_pedido = pd.read_csv("itens_pedido_tratados.csv")
pagamentos = pd.read_csv("pagamentos_tratados.csv")

# =================== 2. Total de vendas por mês ===================
pedidos['data_pedido'] = pd.to_datetime(pedidos['data_pedido'])
pagamentos['data_pagamento'] = pd.to_datetime(pagamentos['data_pagamento'])

vendas_mensais = pagamentos.groupby(pagamentos['data_pagamento'].dt.to_period('M'))['valor_pago'].sum()
vendas_mensais.plot(kind='bar', title="Total de Vendas por Mês", xlabel='Mês', ylabel='Valor Pago (R$)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# =================== 3. Produtos mais vendidos ===================
mais_vendidos = itens_pedido.groupby('id_produto')['quantidade'].sum().sort_values(ascending=False).head(10)
mais_vendidos = mais_vendidos.reset_index().merge(produtos[['id_produto', 'nome']], on='id_produto')
sns.barplot(data=mais_vendidos, x='quantidade', y='nome', palette="viridis")
plt.title("Top 10 Produtos Mais Vendidos")
plt.xlabel("Quantidade Vendida")
plt.ylabel("Produto")
plt.tight_layout()
plt.show()

# =================== 4. Clientes que mais compram ===================
mais_compradores = pedidos['cliente_id'].value_counts().head(10).reset_index()
mais_compradores.columns = ['cliente_id', 'quantidade_pedidos']
mais_compradores = mais_compradores.merge(clientes[['cliente_id', 'nome']], on='cliente_id')
sns.barplot(data=mais_compradores, x='quantidade_pedidos', y='nome', palette="cubehelix")
plt.title("Top 10 Clientes com Mais Pedidos")
plt.xlabel("Quantidade de Pedidos")
plt.ylabel("Cliente")
plt.tight_layout()
plt.show()

# =================== 5. Formas de pagamento mais usadas ===================
formas_pagamento = pagamentos['metodo_pagamento'].value_counts()
formas_pagamento.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=sns.color_palette("Set2"))
plt.title("Formas de Pagamento Mais Usadas")
plt.ylabel('')
plt.tight_layout()
plt.show()

