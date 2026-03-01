📡 TelecomX — Churn Analysis com ETL e EDA
Este projeto explora a rotatividade de clientes em telecomunicações, utilizando um pipeline ETL modular e uma análise exploratória de dados (EDA) para revelar padrões de cancelamento e apoiar estratégias de retenção.

🚀 Objetivo
Entender os principais fatores que levam clientes a cancelar serviços.

Identificar perfis de maior risco de churn.

Fornecer recomendações práticas para reduzir a perda de clientes.

🔄 Arquitetura do Pipeline ETL
O fluxo de dados foi construído em três etapas principais:

Extração → coleta e organização dos dados brutos.

Transformação → limpeza, padronização, conversão de tipos e validações.

Carga → armazenamento em formato estruturado, pronto para análise e modelagem.

📊 Análise Exploratória (EDA)
A exploração dos dados buscou responder perguntas como:

Qual é a taxa geral de churn?

Como variáveis categóricas (contrato, forma de pagamento, serviços adicionais) influenciam o cancelamento?

Quais padrões surgem em variáveis numéricas (tempo de permanência, valor da fatura)?

Existe uma faixa de preço crítica associada ao risco de churn?

🔍 Insights principais
Contratos mensais concentram maior taxa de cancelamento.

Pagamentos via cheque eletrônico estão ligados a maior risco.

Clientes com menor tempo de permanência tendem a cancelar mais.

Ausência de segurança online e suporte técnico aumenta a probabilidade de churn.

Faturas acima de US$ 70/mês revelam maior sensibilidade ao cancelamento.

🏗 Estrutura do Repositório
Código
telecomx-churn-analysis/
│
├── src/              # Scripts ETL
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── notebooks/        # Análises exploratórias
│   └── eda.ipynb
│
├── .gitignore
└── README.md
▶️ Como rodar o projeto
Clone o repositório

bash
git clone https://github.com/barretosilva/telecomx.git
cd telecomx
Crie e ative um ambiente virtual

bash
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows
Instale as dependências

bash
pip install -r requirements.txt
Execute o pipeline ETL

bash
python src/load.py
🛠️ Tecnologias Utilizadas
Linguagem: Python

Bibliotecas: Pandas, NumPy, Matplotlib, Seaborn

Ambiente: Jupyter Notebook

Ferramentas de apoio: VS Code, Git/GitHub

Autor: André Barreto