import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# carregando o dataset
df = pd.read_csv('data/titanic_dataset.csv')

# visualizando as primeiras linhas do dataset e informações gerais
print(df.head())
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

# visualizando a distribuição de sobreviventes por sexo
print("\nSobrevivência por sexo:")
print(df.groupby("Sex")["Survived"].value_counts())

# visualizando a distribuição de sobreviventes por classe
print("\nSobrevivência por classe:")
print(df.groupby("Pclass")["Survived"].value_counts())

# visualizando a distribuição de sobreviventes por idade
print("\nSobrevivência por idade:")
print(df.groupby("Age")["Survived"].value_counts())

# gráfico de barras para sobrevivência por sexo
sns.countplot(x='Sex', hue='Survived', data=df)
plt.title('Sobrevivência por Sexo')
plt.show()

# gráfico de barras para sobrevivência por classe
sns.countplot(x='Pclass', hue='Survived', data=df)
plt.title('Sobrevivência por Classe')
plt.show()

# gráfico de barras para sobrevivência por idade
sns.histplot(df["Age"], bins=30)
plt.show()

# a partir dessa análise inicial, podemos observar que há uma diferença significativa na taxa de sobrevivência entre homens e mulheres, com as mulheres tendo uma taxa de sobrevivência muito maior. Além disso, a classe social também parece influenciar a sobrevivência, com os passageiros da primeira classe tendo uma taxa de sobrevivência mais alta do que os da segunda e terceira classe. A idade também pode ser um fator importante, já que os passageiros mais jovens parecem ter uma taxa de sobrevivência mais alta do que os mais velhos. Esses insights podem ser úteis para entender melhor os fatores que influenciaram a sobrevivência dos passageiros do Titanic.



