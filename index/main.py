# ANÁLISE EXPLORATÓRIA DE DADOS - TITANIC

# Este código realiza uma análise exploratória de dados (EDA) no dataset do Titanic, que contém informações sobre os passageiros e suas chances de sobrevivência. O objetivo é identificar padrões e insights relacionados à sobrevivência dos passageiros com base em variáveis como sexo, classe social e idade.

# Importando as bibliotecas necessárias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# carregando o dataset
df = pd.read_csv('data/titanic_dataset.csv')

# visualizando as primeiras linhas do dataset e informações gerais
print(df.shape)
print(df.columns)
print(df.sample(10))
print(df.info())
print(df.describe())
print(df.dtypes)

# limpando linhas duplicadas
duplicateRows = df[df.duplicated()]
print("\nLinhas duplicadas:\n")
print(duplicateRows)

# verificar dados faltantes
print("\nValores nulos:\n")
print(df.isnull().sum())

# visualizando a distribuição de sobreviventes
print("\nSobrevivência:")
print(df["Survived"].value_counts())

# gráfico de barras para sobrevivência
# sns.countplot(x='Survived', data=df)
# plt.xlabel('Sobrevivência (0 = Não, 1 = Sim)')
# plt.ylabel('Contagem')
# plt.title('Distribuição de Sobreviventes')
# plt.show()

# visualizando a distribuição de sobreviventes por sexo
print("\nSobrevivência por sexo:")
print(df.groupby("Sex")["Survived"].value_counts())

# gráfico de barras para sobrevivência por sexo
# sns.countplot(x='Sex', data=df)
# plt.xlabel('Sexo')
# plt.ylabel('Contagem')
# plt.title('Sobrevivência por Sexo')
# plt.show()

# ===========================================================
# INSIGHTS:
# ===========================================================
# A partir da análise inicial, podemos observar que a maioria dos passageiros não sobreviveu (0) em comparação com os que sobreviveram (1). Além disso, a taxa de sobrevivência é significativamente maior entre as mulheres do que entre os homens, o que pode indicar que as mulheres tiveram prioridade no embarque nos botes salva-vidas. Esses insights sugerem que o sexo dos passageiros foi um fator importante na sobrevivência, e isso pode ser explorado mais a fundo em análises subsequentes, como a relação entre sexo e classe social, ou sexo e idade. 
# ===========================================================

# visualizando a distribuição de sobreviventes por classe
print("\nSobrevivência por classe:")
print(df.groupby("Pclass")["Survived"].value_counts())

# gráfico de barras para sobrevivência por classe
# sns.countplot(x='Pclass', hue='Survived', data=df)
# plt.xlabel('Classe Social')
# plt.ylabel('Contagem')
# plt.title('Sobrevivência por Classe')
# plt.show()

# ===========================================================
# INSIGHTS:
# ===========================================================
# A análise da sobrevivência por classe social revela que os passageiros da primeira classe tiveram uma taxa de sobrevivência significativamente maior do que os passageiros da segunda e terceira classe. Isso pode ser atribuído a vários fatores, como o acesso mais fácil aos botes salva-vidas, a localização das cabines e a prioridade dada aos passageiros de classes superiores durante o processo de evacuação. Esses insights sugerem que a classe social foi um fator crucial na sobrevivência dos passageiros do Titanic, e isso pode ser explorado mais a fundo em análises subsequentes, como a relação entre classe social e sexo, ou classe social e idade. 
# ===========================================================

# visualizando a distribuição de sobreviventes por idade
print("\nSobrevivência por idade:")
df["Age_int"] = df["Age"].round()
print(df.groupby("Age_int")["Survived"].value_counts())

# gráfico de barras para sobrevivência por idade
# sns.histplot(df["Age_int"], bins=30, multiple="stack")
# plt.title('Sobrevivência por Idade')
# plt.xlabel('Idade')
# plt.ylabel('Contagem')
# plt.show()

# visualizando a distribuição por faixa etária
bins = [0, 12, 18, 35, 60, 100]
labels = ["Criança", "Adolescente", "Jovem Adulto", "Adulto", "Idoso"]
df["Age_group"] = pd.cut(df["Age"], bins=bins, labels=labels)
print("\nSobrevivência por faixa etária:")
print(df.groupby("Age_group")["Survived"].value_counts())

# gráfico de barras para sobrevivência por faixa etária
# sns.countplot(x='Age_group', data=df)
# plt.title('Sobrevivência por Faixa Etária')
# plt.xlabel('Faixa Etária')
# plt.ylabel('Contagem')
# plt.show()

# ===========================================================
# INSIGHTS:
# ===========================================================
# A análise da sobrevivência por idade revela que os passageiros mais jovens, especialmente crianças e adolescentes, tiveram uma taxa de sobrevivência mais alta em comparação com os adultos e idosos. Isso pode ser atribuído a vários fatores, como a prioridade dada às crianças durante o processo de evacuação e a maior mobilidade dos passageiros mais jovens. Esses insights sugerem que a idade foi um fator importante na sobrevivência dos passageiros do Titanic, e isso pode ser explorado mais a fundo em análises subsequentes, como a relação entre idade e sexo, ou idade e classe social.
# ===========================================================

# visualizando a relação entre sexo, classe social e sobrevivência
print("\nSobrevivência por sexo e classe social:")
print(df.groupby(["Sex", "Pclass"])["Survived"].value_counts())

# gráfico de barras para sobrevivência por sexo e classe social
sns.catplot(
    x="Pclass",
    y="Survived",
    hue="Sex",
    kind="bar",
    data=df
)

plt.xlabel("Classe Social")
plt.ylabel("Taxa de Sobrevivência")
plt.title("Sobrevivência por Classe Social e Sexo")
plt.show()

# ===========================================================
# INSIGHTS:
# ===========================================================
# A análise da sobrevivência por sexo e classe social revela que as mulheres da primeira classe tiveram a maior taxa de sobrevivência, seguidas pelas mulheres da segunda classe e, por último, pelas mulheres da terceira classe. Entre os homens, a taxa de sobrevivência foi significativamente menor em todas as classes, com os homens da terceira classe apresentando a menor taxa de sobrevivência. Esses insights sugerem que tanto o sexo quanto a classe social foram fatores cruciais na sobrevivência dos passageiros do Titanic, e que a combinação desses fatores teve um impacto significativo nas chances de sobrevivência.
# ===========================================================