## Repositório

Este projeto também está disponível no GitHub para fins de versionamento e consulta:

https://github.com/samuelbucco/titanic

# 🚢 Análise Exploratória de Dados – Titanic

## 📊 Descrição do Projeto

Este projeto tem como objetivo realizar uma **Análise Exploratória de Dados (AED)** utilizando a base de dados pública do desastre do Titanic.

A análise busca compreender o comportamento das variáveis presentes no dataset e identificar **padrões, relações e fatores associados à sobrevivência dos passageiros**.

Durante o processo foram realizadas:

* exploração inicial da base de dados
* análise estatística descritiva
* visualização de dados
* comparação entre grupos de passageiros
* identificação de possíveis fatores relacionados à sobrevivência

---

## 📁 Dataset

O dataset utilizado contém informações sobre os passageiros do Titanic, incluindo:

* Classe social (`Pclass`)
* Sexo (`Sex`)
* Idade (`Age`)
* Número de familiares a bordo (`SibSp` e `Parch`)
* Porto de embarque (`Embarked`)
* Tarifa paga (`Fare`)
* Status de sobrevivência (`Survived`)

A base de dados está disponível publicamente e foi utilizada em formato **CSV**.

---

## 🛠 Tecnologias Utilizadas

As análises foram realizadas utilizando:

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn

O desenvolvimento foi realizado no **Visual Studio Code**.

---

## 🔎 Etapas da Análise

A análise exploratória foi conduzida nas seguintes etapas:

1. Importação das bibliotecas necessárias
2. Carregamento da base de dados
3. Verificação da estrutura do dataset
4. Identificação de valores ausentes
5. Análise estatística descritiva
6. Visualização gráfica das variáveis
7. Comparação entre grupos de passageiros
8. Extração de insights relevantes

---

## 📈 Exemplos de Análises Realizadas

Algumas análises exploradas neste projeto incluem:

* Distribuição da idade dos passageiros
* Sobrevivência por sexo
* Sobrevivência por classe social
* Relação entre sexo e classe na taxa de sobrevivência
* Análise de sobrevivência por faixa etária

Essas análises foram realizadas por meio de gráficos e estatísticas descritivas.

---

## 💡 Principais Insights

A análise exploratória revelou alguns padrões importantes:

* Mulheres apresentaram taxas de sobrevivência significativamente maiores que homens.
* Passageiros da **primeira classe** tiveram maiores chances de sobrevivência em comparação com os da terceira classe.
* Crianças tiveram maior probabilidade de sobrevivência em relação aos adultos.
* A combinação entre **sexo e classe social** mostrou forte influência nas chances de sobrevivência.

Esses resultados sugerem que fatores sociais e estruturais influenciaram o processo de evacuação durante o desastre.

---

## 📌 Conclusão

A Análise Exploratória de Dados permitiu compreender melhor a estrutura do dataset e identificar padrões relevantes relacionados à sobrevivência dos passageiros.

Este projeto demonstra como ferramentas de análise de dados podem ser utilizadas para **extrair informações significativas a partir de dados históricos**.

---

## Como executar

1. Criar ambiente virtual
2. Instalar dependências

pip install -r requirements.txt

3. Executar o script

python index/AED_titanic.py

## 👨‍💻 Autor

Samuel Bucco
