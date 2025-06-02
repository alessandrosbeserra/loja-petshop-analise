import pandas as pd
from sqlalchemy import create_engine
import numpy as np

# 🔒 Configuração da conexão com MySQL via SQLAlchemy
usuario = 'root'
senha = 'root'
host = 'localhost'
porta = '3306'
banco = 'loja_petshop'

# Criar a engine de conexão
engine = create_engine(f'mysql+mysqlconnector://{usuario}:{senha}@{host}:{porta}/{banco}')

# Função para buscar dados e retornar DataFrame
def consultar_tabela(tabela):
    return pd.read_sql(f"SELECT * FROM {tabela};", con=engine)

# ================== Tratamentos ==================

# 1. Clientes
clientes = consultar_tabela('clientes')
clientes['nome'] = clientes['nome'].str.strip()
clientes['email'] = clientes['email'].fillna('email_nao_informado@example.com')
clientes['telefone'] = clientes['telefone'].fillna('Telefone não informado')

# 2. Produtos
produtos = consultar_tabela('produtos')
produtos['estoque'] = produtos['estoque'].apply(lambda x: max(0, x))
produtos['preco'] = produtos['preco'].replace(0, np.nan)
produtos['preco'] = produtos['preco'].fillna(produtos['preco'].mean())

# 3. Pedidos
pedidos = consultar_tabela('pedidos')
pedidos['status'] = pedidos['status'].str.strip()
pedidos['data_pedido'] = pd.to_datetime(pedidos['data_pedido'], errors='coerce')

# 4. Itens do Pedido
itens_pedido = consultar_tabela('itens_pedido')
itens_pedido['quantidade'] = itens_pedido['quantidade'].apply(lambda x: max(1, x))
itens_pedido['preco_unitario'] = itens_pedido['preco_unitario'].apply(lambda x: max(0, x))

# 5. Pagamentos
pagamentos = consultar_tabela('pagamentos')
pagamentos['valor_pago'] = pagamentos['valor_pago'].apply(lambda x: max(0, x))
pagamentos['data_pagamento'] = pd.to_datetime(pagamentos['data_pagamento'], errors='coerce')

# ================== Exportar para CSV ==================

clientes.to_csv('clientes_tratados.csv', index=False)
produtos.to_csv('produtos_tratados.csv', index=False)
pedidos.to_csv('pedidos_tratados.csv', index=False)
itens_pedido.to_csv('itens_pedido_tratados.csv', index=False)
pagamentos.to_csv('pagamentos_tratados.csv', index=False)

print("✅ Tratamento de dados concluído com sucesso.")

