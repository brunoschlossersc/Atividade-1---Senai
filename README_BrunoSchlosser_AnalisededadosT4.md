# Atividade-1---Senai
Projeto da atividade 1 do Senai
# Mini-Projeto Avaliativo: Análise Exploratória de Dados (AED) - Varejo

**Aluno:** [Seu Nome Completo]  
**Turma:** Analise_de_Dados_T1  
**Módulo:** 1 - Semana 07  

---

## 📌 Descrição do Projeto

Este projeto consiste em uma **Análise Exploratória de Dados (AED)** aplicada a uma base de dados de Varejo contendo registros de transações comerciais. O objetivo principal foi realizar o saneamento, tratamento de dados brutos (limpeza de nulos, inconsistências e conversão de tipos) e a geração de estatísticas descritivas/agrupamentos para extrair insights úteis para tomada de decisão em negócios e visualização de dados (BI).

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
* Python 3.8+ instalado ou acesso ao [Google Colab](https://colab.research.google.com/).
* Biblioteca `pandas` e `numpy` instaladas.

### Passos para Execução no VSCode / Terminal:
1. Clone este repositório:
   ```bash
   git clone [https://github.com/SeuUsuario/Miniprojeto_SeuNome_Analise_de_Dados_T1.git](https://github.com/SeuUsuario/Miniprojeto_SeuNome_Analise_de_Dados_T1.git)

    Acesse a pasta do projeto e coloque o arquivo Varejo.csv na raiz do diretório.

    Instale as dependências necessárias:
    Bash

    pip install pandas numpy

    Execute o script principal:
    Bash

    python miniprojeto_varejo.py

🛠️ Detalhamento das Sprints de Desenvolvimento

    Sprint 1 (Importação dos dados): Leitura da base Varejo.csv com Pandas e inspeção inicial de formato, colunas e tipos primitivos de dados.

    Sprint 2 (Transformação de Strings, Inteiros e Datetime): Limpeza e higienização de strings (remoção de espaços duplos e padronização de maiúsculas/minúsculas) e conversão da coluna de data para o tipo datetime.

    Sprint 3 (Limpeza de Nulos e Duplicatas): Remoção de registros duplicados e imputação de valores ausentes (utilização da mediana para variáveis numéricas e rótulo de imputação categórica).

    Sprint 4 (Estatística Descritiva): Cálculo dos parâmetros estatísticos centrais e de dispersão (média, mediana, desvio padrão, moda, quartis Q1-Q3, máx e mín) para a variável Numero_Filhos.

    Sprint 5 (Relatório e Documentação): Criação das tabelas dinâmicas/agrupamentos com groupby() para avaliar volume e ticket médio de vendas, exportação do arquivo sanitizado (Varejo_Tratado.csv) e redação das conclusões da análise.

    Sprint 6 (Versionamento): Organização do histórico do Git e publicação no GitHub público.

📊 Principais Conclusões e Insights

    Tratamento e Qualidade: A sanitização inicial reduziu ruídos e inconsistências que poderiam comprometer relatórios estatísticos e dashboards.

    Distribuição do Perfil de Clientes: A estatística da variável de número de filhos indicou baixa dispersão e forte concentração nos quartis inferiores.

    Agrupamentos Comerciais: O cruzamento das vendas por agrupamentos revelou as categorias e perfis de maior representatividade no faturamento total.


---

## 3. Instruções de Versionamento Git (Sprint 6)

Para atender ao critério de **histórico de commits evolutivos** (e **não fazer tudo em um único commit**), siga a sequência de comandos abaixo no terminal:

```bash
# 1. Inicializar o repositório local e configurar a branch principal
git init
git branch -M main

# 2. Commit da Sprint 1: Carregamento do projeto e dados
git add miniprojeto_varejo.py Varejo.csv
git commit -m "feat(Sprint 1): Adiciona script inicial e importação da base de dados"

# 3. Commit da Sprint 2 & 3: Limpeza e Tratamento
git add miniprojeto_varejo.py
git commit -m "fix(Sprint 2 e 3): Aplica funções de limpeza de texto, remoção de duplicatas e imputação de nulos"

# 4. Commit da Sprint 4 & 5: Estatísticas e Agrupamento
git add miniprojeto_varejo.py
git commit -m "feat(Sprint 4 e 5): Adiciona cálculos de estatística descritiva e agrupamento de vendas"

# 5. Commit do README e documentação final
git add README_SeuNome_Analise_de_Dados_T1.md
git commit -m "docs(Sprint 5 e 6): Adiciona README detalhado com instruções de uso e insights do projeto"

# 6. Conectar ao repositório público do seu GitHub e subir as alterações
# Padrão de nome exigido: Miniprojeto_NomeAluno_Analise_de_Dados_T1
git remote add origin 
