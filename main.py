import pandas as pd
import sqlite3

def convert_types(df):
    for col in df.columns:  # itera colunas do DataFrame
        if pd.api.types.is_numeric_dtype(df[col]):
            # Verifica valores que podem ser convertidos para inteiros
            if (df[col].notnull() & (df[col] % 1 == 0)).all(): # interseção lógica
                try:
                    df[col] = df[col].astype('Int64')
                except Exception as e:
                    print(f"Erro ao converter a coluna {col} para Int64: {e}")
            else:
                df[col] = df[col].astype('float64')  # Mantém como float64
    return df

EXT = ".csv"
listArqCsv = ["representantes", "fornecedores", "produtos", "compras"]  # nomes dos arquivos CSV

# abrir conexao com BD
with sqlite3.connect("database/Loja.db") as conn:
    for nameArq in listArqCsv: #iterar lista de nome dos arq.
        try:
            # Ler o CSV
            print(f"Lendo o arquivo {nameArq}{EXT}...")
            df = pd.read_csv(f"arqCsv/{nameArq}{EXT}", sep=';', na_values=['', ' '])

            if df.empty:
                print(f"O arquivo {nameArq} está vazio ou mal formatado.")
                continue

            for col in df.columns: #iterar colunas
                if df[col].dtype == 'object':
                    # tentativa de conversão p/ numerico
                    converted_col = pd.to_numeric(df[col].str.replace(',', '.'), errors='coerce')
                    
                    if converted_col.notnull().all():
                        df[col] = converted_col # converte, caso sucesso

            # Converter numericos(numeric,integer)
            df = convert_types(df)
            df.drop_duplicates(inplace=True) # remover duplicatas
            # Salvar o DataFrame no banco de dados
            df.to_sql(nameArq, conn, if_exists='replace', index=False)
            print(f"Tabela {nameArq} inserida no DB.")
        except Exception as e:
            print(f"Erro ao processar {nameArq}: {e}")
    print("Tabelas inseridas com sucesso!")
