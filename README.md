# FIAP_FASE5_CAP1

# Análise Preditiva de Rendimento de Safra

Este repositório contém uma análise preditiva do rendimento de safra utilizando diferentes algoritmos de aprendizado de máquina. O objetivo é prever o rendimento das safras com base em variáveis ambientais e meteorológicas, utilizando técnicas avançadas de modelagem, como **Random Forest**, **Gradient Boosting**, **SVM**, e **Redes Neurais**.

A solução envolve um estudo completo, desde a análise exploratória dos dados até a implementação e avaliação de modelos de previsão. Todos os passos, bem como a descrição dos métodos e resultados obtidos, estão detalhados em um **Jupyter Notebook**.

## Visão Geral da Solução

### Etapas da Análise:
1. **Pré-processamento dos Dados**: 
   - Tratamento de dados ausentes e variáveis categóricas.
   - Normalização e escalonamento dos dados para melhorar a performance dos modelos.
   
2. **Análise Exploratória de Dados (EDA)**:
   - Análise de correlações e distribuição das variáveis.
   - Identificação de padrões e insights iniciais dos dados.

3. **Clusterização**:
   - Identificação de grupos ou clusters de dados com o algoritmo K-Means para descobrir padrões ou características comuns entre as amostras.

4. **Modelagem Preditiva**:
   - Construção e avaliação de diferentes modelos preditivos (Regressão Linear, Random Forest, Gradient Boosting, SVM, Redes Neurais).
   - Ajuste de hiperparâmetros utilizando técnicas de otimização como **GridSearchCV**.
   - Avaliação do desempenho dos modelos com métricas como **MAE**, **MSE** e **R²**.

5. **Resultados e Conclusões**:
   - Comparação entre os diferentes modelos.
   - Análise das limitações do trabalho e possíveis melhorias.

## Como Explorar a Solução

Para entender completamente o passo a passo e os detalhes da análise, por favor, consulte o **Jupyter Notebook** localizado no diretório `notebooks/`. O notebook contém a descrição detalhada de todas as etapas do trabalho, incluindo código, gráficos e resultados.

### Acessando o Jupyter Notebook

1. **Pré-requisitos**: Certifique-se de ter o Python instalado em seu ambiente, juntamente com as bibliotecas necessárias. Você pode instalar as dependências utilizando o comando:
   
   ```bash
   pip install -r requirements.txt

2. Iniciar o Jupyter Notebook: Navegue até o diretório do repositório e execute o seguinte comando para abrir o notebook:

   ```bash
   jupyter notebook

3. Abra o notebook localizado no diretório notebooks/ para visualizar o passo a passo completo.

### Resultados Principais
Os modelos preditivos avaliados mostraram uma variação significativa no desempenho. O Gradient Boosting obteve o melhor desempenho, seguido pelo Random Forest. Modelos como SVM e Redes Neurais não performaram tão bem devido à natureza dos dados e às dificuldades de ajuste de parâmetros.

### Vídeo Demonstrativo
Para uma demonstração visual de todo o processo de execução do código e análise, veja o vídeo abaixo:

[Inserir Link do YouTube Aqui]
