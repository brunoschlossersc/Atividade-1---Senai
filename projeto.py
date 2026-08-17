import re
import numpy as np
import pandas as pd

# Parte 1: IMPORTAÇÃO E INSPEÇÃO INICIAL DOS DADOS

print("Parte 1: Carregamento e Inspeção Inicial da Base de Dados")
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
# Partes 2 e 3: Tratamento de dados - Dados duplicados e incompletos
# ==============================================================================
print("\n" + "=" * 60)
print("Partes 2 e 3: Identificação de Problemas, Limpeza e Transformação")
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
    def limpar_texto(texto):
    if pd.isna(texto):
        return texto
    texto = str(texto).strip()  # Remove espaços nas pontas
    texto = re.sub(r"\s+", " ", texto)  # Remove espaços duplos
    return texto.title()  # Padroniza Capitalização


# Aplicar limpeza de string em colunas do tipo object
colunas_texto = df_limpo.select_dtypes(include=["object"]).columns
for col in colunas_texto:
    # Evitar aplicar na coluna de Data por enquanto
    if "data" not in col.lower():
        df_limpo[col] = df_limpo[col].apply(limpar_texto)

# Identificar e padronizar coluna de Data (ex: 'Data', 'data_compra', 'DATA')
col_data = [c for c in df_limpo.columns if "data" in c.lower()]
if col_data:
    nome_col_data = col_data[0]
    # Converter para Datetime
    df_limpo[nome_col_data] = pd.to_datetime(
        df_limpo[nome_col_data], errors="coerce"
    )
    print(f"✅ Coluna '{nome_col_data}' convertida para datetime.")

# Tratamento de valores monetários/numéricos se formatados como texto (ex: 'R$ 100,50')
col_valor = [
    c
    for c in df_limpo.columns
    if any(k in c.lower() for k in ["valor", "preco", "preço", "venda"])
]
if col_valor:
    nome_col_valor = col_valor[0]
    if df_limpo[nome_col_valor].dtype == "object":
        df_limpo[nome_col_valor] = (
            df_limpo[nome_col_valor]
            .astype(str)
            .str.replace("R$", "", regex=False)
            .str.replace(".", "", regex=False)
            .str.replace(",", ".", regex=False)
            .str.strip()
        )
        df_limpo[nome_col_valor] = pd.to_numeric(
            df_limpo[nome_col_valor], errors="coerce"
        )
        print(f"✅ Coluna '{nome_col_valor}' tratada e convertida para float.")

# Tratamento de Remoção de Duplicatas
if duplicatas_iniciais > 0:
    df_limpo = df_limpo.drop_duplicates()
    print(
        f"✅ {duplicatas_iniciais} registros duplicados removidos com sucesso."
    )

# Tratamento de Nulos (Estratégia Escolhida)
# - Colunas categóricas vazias: preenchidas com "Não Informado"
# - Colunas numéricas (ex: número de filhos): imputação pela Mediana (resiliente a outliers)
col_filhos = [
    c
    for c in df_limpo.columns
    if any(k in c.lower() for k in ["filho", "filhos", "qtd_filhos"])
]
nome_col_filhos = col_filhos[0] if col_filhos else "Numero_Filhos"

if nome_col_filhos in df_limpo.columns:
    mediana_filhos = df_limpo[nome_col_filhos].median()
    df_limpo[nome_col_filhos] = df_limpo[nome_col_filhos].fillna(mediana_filhos)
    print(
        f"✅ Nulos na coluna '{nome_col_filhos}' imputados pela mediana ({mediana_filhos})."
    )

# Preencher demais nulos categóricos restantes
for col in df_limpo.select_dtypes(include=["object"]).columns:
    df_limpo[col] = df_limpo[col].fillna("Não Informado")

print(
    f"Total de nulos na base após limpeza: {df_limpo.isnull().sum().sum()}\n"
)
    if pd.isna(texto):
        return texto
    texto = str(texto).strip()  # Remove espaços nas pontas
    texto = re.sub(r"\s+", " ", texto)  # Remove espaços duplos
    return texto.title()  # Padroniza Capitalização
