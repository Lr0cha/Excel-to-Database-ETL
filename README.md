# Excel-to-Database-ETL

Este projeto realiza o processo de Extração, Transformação e Carga (ETL) de dados de arquivos Excel para um banco de dados. O fluxo de trabalho inclui a extração dos dados de uma tabela em Excel, convertido para o formato CSV, o processamento com Python e, finalmente, a carga dos dados em um banco de dados SQLite.

## O que foi utilizado para concluir o propósito:
- **Python**: Linguagem de programação utilizada para o processamento de dados.
- **Pandas**: Biblioteca para manipulação e análise de dados.
- **SQLite**: Banco de dados utilizado para armazenar os dados processados.
- **CSV**: Formato de arquivo para facilitar a manipulação de dados.

## Etapas do Processo ETL

### 1. Extração
- Os dados foram extraídos de planilhas Excel e convertidos para o formato CSV.

### 2. Transformação
- Os dados em formato CSV são lidos usando a biblioteca Pandas.
- Durante a transformação, são realizadas as seguintes operações:
  - Limpeza de dados (remoção de duplicatas, tratamento de valores ausentes).
  - Conversão de tipos de dados (ex.: texto para numérico).

### 3. Carga
- Os dados processados são carregados em um banco de dados SQLite.
- As operações incluem a criação de novas tabelas e inserção dos dados.

##
Sinta-se à vontade para contribuir com melhorias ou utiliza-lo!
