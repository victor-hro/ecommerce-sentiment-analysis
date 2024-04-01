Claro! Aqui está o README atualizado com as informações sobre o web app do Streamlit:

```markdown
# Olist Sentiment Analysis

## Descrição do Projeto

Este projeto implementa uma análise de sentimentos para avaliações de produtos da plataforma Olist.
Ele inclui funcionalidades para pré-processamento de dados, treinamento de modelos e previsão de sentimentos.

## Estrutura do Projeto

```
projeto/
└── src/
    ├── config/
    ├── dataset/
    ├── experiments/
    ├── preprocessing/
    ├── saved models/
    ├── pipeline.py
    ├── predict.py
    ├── training_pipeline.py
    └── app.py
```

- **config:** Contém arquivos de configuração para o projeto.
- **dataset:** Contém os dados usados no projeto.
- **experiments:** Contém resultados e registros de experimentos.
- **preprocessing:** Contém scripts para pré-processamento de dados.
- **saved models:** Contém modelos treinados salvos.

## Funcionalidades Principais

- **pipeline.py:** Implementa o pipeline principal do projeto.
- **predict.py:** Implementa a funcionalidade de previsão.
- **training_pipeline.py:** Implementa o pipeline de treinamento do modelo.
- **app.py:** Implementa um web app usando Streamlit para interagir com o modelo de análise de sentimentos.

## Setup

Para configurar o projeto, execute os seguintes comandos:

```bash
python setup.py sdist bdist_wheel
pip install -e .
```

## Como Usar o Web App

1. Clone este repositório para sua máquina local.
2. Navegue até o diretório onde o repositório foi clonado.
3. Instale as dependências do projeto executando o comando `pip install -r requirements.txt`.
4. Execute o web app usando o comando `streamlit run app.py`.
5. O web app será aberto em seu navegador padrão.
6. Insira o nome do produto e seu comentário no formulário apresentado.
7. Clique no botão "Enviar Dados" para submeter os dados e visualizar a previsão de sentimento.

--

<p align="center">
  <img src="images/app.png" alt="web app" />
</p>

--