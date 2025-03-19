
# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# FIAP Fase5_Cap1 FarmTech na era da cloud computing



## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/in/amanda-fragnan-b61537255/" target="_blank">Amanda Fragnan RM 555684 </a>
- <a href="https://www.linkedin.com/in/cunhaandre/" target="_blank">Andre Cunha RM 560648</a>
- <a href="https://www.linkedin.com/in/gabriellehalasc/" target="_blank">Gabrielle Halasc RM 560147</a> 

## 👩‍🏫 Professores:
### Tutor(a)
- <a href="https://www.linkedin.com/in/lucas-gomes-moreira-15a8452a/">Lucas Gomes Moreira</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/in/profandregodoi/">André Godoi</a>

## 📜 Descrição
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

### Resultados Principais
Os modelos preditivos avaliados mostraram uma variação significativa no desempenho. O Gradient Boosting obteve o melhor desempenho, seguido pelo Random Forest. Modelos como SVM e Redes Neurais não performaram tão bem devido à natureza dos dados e às dificuldades de ajuste de parâmetros.

### Vídeo Demonstrativo
Para uma demonstração visual de todo o processo de execução do código e análise, veja o vídeo abaixo:

[https://youtu.be/2a308ChhgUg]

## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:


- <b>AmandaFragnanDeOliveira_rm555684_pbl_fase5.ipynb</b>: aqui esta o arquivo com o Notebook Python.

- <b>rrendimento_da_colheita.csv</b>: arquivo utilizado para executar o Notebook contendo os dados da colheita.

- <b>README.md</b>: arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).


## 🔧 Como executar o código

Para entender completamente o passo a passo e os detalhes da análise, por favor, consulte o **Jupyter Notebook** localizado no diretório `notebooks/`. O notebook contém a descrição detalhada de todas as etapas do trabalho, incluindo código, gráficos e resultados.

### Acessando o Jupyter Notebook

1. **Pré-requisitos**: Certifique-se de ter o Python instalado em seu ambiente, juntamente com as bibliotecas necessárias. Você pode instalar as dependências utilizando o comando:
   
   ```bash
   pip install -r requirements.txt

2. Iniciar o Jupyter Notebook: Navegue até o diretório do repositório e execute o seguinte comando para abrir o notebook:

   ```bash
   jupyter notebook

3. Abra o notebook localizado no diretório para visualizar o contéudo completo.

### Custos para armazenamento dessa estrutura em nuvem

 Conforme a estimativa realizada na Calculadora da AWS, os custos mensais para uma instância t4g.micro com 50GB de armazenamento são:

- Região São Paulo (sa-east-1): USD 17,38/mês
- Região Virgínia do Norte (us-east-1): USD 10,13/mês
  ![Gráfico](https://github.com/AmandaFragnan/FIAP_FASE5_CAP1/blob/main/Captura%20de%20tela%202025-03-18%20163209.png)
  
   A região dos EUA apresenta um custo aproximadamente 41,7% menor em comparação com a região brasileira. No entanto, o custo não é o único fator a ser considerado.
   A API que processará dados de sensores precisa de respostas rápidas e baixa latência. A escolha de servidores mais próximos aos usuários melhora a velocidade de acesso aos dados e reduz atrasos na comunicação entre sensores e a nuvem. Então devemos levar em conta que a região São Paulo irá ter uma melhor comunicação com os servidores, oferencendo até 3x mais velocidade aos usuarios do Brasil do que a da Virginia.
   Outros pontos a serem considerados são  as legislações brasileiras, como a Lei Geral de Proteção de Dados (LGPD), que podem exigir que determinados dados sejam armazenados dentro do país. Caso os sensores capturem informações sensíveis, a transferência para servidores no exterior pode representar riscos de não conformidade legal.
Manter os dados na região de São Paulo garante aderência às normas locais, evitando problemas jurídicos e protegendo informações críticas.
   Levando em consideração os pontos apresentados podemos dizer que embora a região da Virgínia do Norte tenha um custo inferior, a região de São Paulo é a melhor escolha devido a:
- Menor latência e melhor desempenho para usuários no Brasil.
- Conformidade com a legislação brasileira (LGPD).
- Maior segurança jurídica ao manter os dados dentro do país.

Portanto, a recomendação final é hospedar a API e os dados na região de São Paulo (sa-east-1) para garantir um serviço rápido, seguro e alinhado às exigências legais.

Link Youtube: 
https://youtu.be/rFq2N4gGdZk

## Historico de lançamentos

- <b> 0.1.0 -07/03/2025<b>
- <b> 0.1.1 -18/03/2025<b>

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
