import re
import numpy as np
import pandas as pd

# Parte 1: IMPORTAÇÃO E INSPEÇÃO INICIAL DOS DADOS

print("SPRINT 1: Carregamento e Inspeção Inicial da Base de Dados")
print("=" * 60)

# Path do arquivo (ajuste o caminho de acordo com seu ambiente/Colab/VSCode)
file_path = "Varejo.csv"

try:
    df = pd.read_csv(file_path)
    print("✅ Base de dados carregada com sucesso!\n")
except FileNotFoundError:
    print(
        f"❌ Arquivo '{file_path}' não encontrado. Certifique-se de que o arquivo está no mesmo diretório."
    )
    # Exemplo genérico fallback para demonstração
    exit()

# Exibir dimensões da base
print(f"Número de Registros (Linhas): {df.shape[0]}")
print(f"Número de Colunas: {df.shape[1]}\n")

print("--- Nomes das Colunas e Tipos Originais de Dados ---")
print(df.dtypes)
print("\n--- Primeiras 5 linhas ---")
print(df.head())
