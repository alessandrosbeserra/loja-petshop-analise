
# 🐾 Projeto de Análise de Dados - Loja Petshop

Este projeto simula a operação de uma loja virtual de petshop, com foco em um pipeline completo de **ETL**, **tratamento**, **análise exploratória** e **visualização de dados**. O objetivo é transformar dados brutos em **insights de negócio** que possam apoiar a tomada de decisão.

## 📌 Descrição do Projeto

Neste projeto, simulamos o banco de dados de uma loja de petshop contendo informações sobre:
- Clientes
- Produtos
- Pedidos
- Itens do pedido
- Pagamentos

Foram realizadas análises como:
- Total de vendas por mês
- Produtos mais vendidos
- Clientes que mais compram
- Formas de pagamento mais usadas

## 🧰 Tecnologias Utilizadas

- **MySQL** – Criação e manipulação do banco de dados
- **Python** – Coleta, tratamento e análise de dados
  - `pandas`, `matplotlib`, `seaborn`
- **Power BI** – Visualização de dados (opcional)
- **Git/GitHub** – Controle de versão e publicação do projeto
- **Jupyter Notebook / PyCharm** – Ambiente de desenvolvimento

## 🔄 Pipeline de Dados (ETL + Análise)

### 1. Extração
- Dados extraídos do MySQL usando `pymysql` e `pandas`.

### 2. Transformação (Tratamento)
- Preenchimento de valores ausentes (`fillna`)
- Conversão de datas
- Padronização de campos

### 3. Carga
- Dados tratados salvos como arquivos `.csv` organizados por tabela.

### 4. Análise Exploratória
- Análise com gráficos para entender o comportamento de vendas, produtos e clientes.

### 5. Visualização de Insights
- Gráficos de barras, pizza e linha para facilitar a interpretação.

## 📊 Exemplos de Gráficos (Screenshots)

| Vendas por mês | Produtos mais vendidos |
|----------------|------------------------|
| ![vendas_mes](img/vendas_por_mes.png) | ![produtos_vendidos](img/produtos_mais_vendidos.png) |

| Clientes que mais compram | Formas de pagamento |
|---------------------------|---------------------|
| ![clientes](img/clientes_mais_compram.png) | ![pagamento](img/formas_pagamento.png) |


## 🚀 Como Executar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/alessandrosbeserra/loja-petshop-analise.git
   ```

2. Crie o ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate.bat  # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute os scripts:
   - `extrair_dados.py`
   - `tratamento_dados.py`
   - `exploracao_dados.py`

## 📝 Autor

**Alessandro — Data Analyst em formação**

## ☁️ Próximos Passos

- Implementar dashboard interativo com Power BI
- Realizar previsão de vendas (Machine Learning)
- Incluir dados financeiros e de estoque

---

## 🐍 Pronto para transformar dados em decisões!
