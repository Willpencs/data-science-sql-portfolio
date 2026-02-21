# 🏗️ Pipeline ETL de Dados Financeiros

Este projeto demonstra a implementação de um pipeline **ETL (Extract, Transform, Load)** automatizado em Python, focado na coleta e tratamento de dados do mercado financeiro.

## 🚀 Fluxo de Trabalho

1. **Extração (Extract):** Simulação de consumo de dados de ativos financeiros (PETR4, VALE3, ITUB4, ABEV3).
2. **Transformação (Transform):** - Identificação e tratamento de valores ausentes (NaN). No caso do ativo `ABEV3`, foi aplicada a **imputação pela média** para garantir a integridade estatística.
   - Adição de metadados (`extracted_at`) para rastreabilidade do processamento.
3. **Carga (Load):** Persistência dos dados higienizados em um banco de dados relacional **SQLite**.

## 🛠️ Tecnologias Utilizadas

* **Python 3.10+**
* **Pandas:** Manipulação e limpeza de dados.
* **SQLite3:** Armazenamento relacional e consultas SQL.
* **WSL (Ubuntu):** Ambiente de desenvolvimento e execução.
* Nota de Ambiente: Este projeto foi desenvolvido e validado em ambiente WSL (Ubuntu), garantindo compatibilidade com sistemas baseados em Unix e facilitando a conteinerização futura.

## 📂 Como Executar

1. Certifique-se de ter as dependências instaladas:
   ```bash
   pip install -r requirements.txt

2. Execute o pipeline:
   python3 etl_pipeline.py

3. O arquivo 'market_data.db' será gerado automaticamente com os dados processados.
   
