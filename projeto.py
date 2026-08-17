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

# ==============================================================================
# SPRINT 2 & 3: TRATAMENTO DE STRINGS, DATAS, NUMÉRICOS, NULOS E DUPLICATAS
# ==============================================================================
print("\n" + "=" * 60)
print("SPRINT 2 & 3: Identificação de Problemas, Limpeza e Transformação")
print("=" * 60)

# 1. Identificação de Valores Nulos e Duplicatas Iniciais
nulos_iniciais = df.isnull().sum()
duplicatas_iniciais = df.duplicated().sum()

print("--- Diagnóstico Inicial ---")
print("Valores Nulos por Coluna:")
print(nulos_iniciais[nulos_iniciais > 0])
print(f"\nTotal de Linhas Duplicadas Detectadas: {duplicatas_iniciais}\n")

# Copia de segurança para transformações
df_limpo = df.copy()


# Função para limpeza de textos/strings
def limpar_texto(texto):
    if pd.isna(texto):
        return texto
    texto = str(texto).strip()  # Remove espaços nas pontas
    texto = re.sub(r"\s+", " ", texto)  # Remove espaços duplos
    return texto.title()  # Padroniza Capitalização
