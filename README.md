# Olist Sentiment Analysis

## Descrição do Projeto

Este projeto implementa uma análise de sentimentos para avaliações de produtos da plataforma Olist. Ele inclui funcionalidades para pré-processamento de dados, treinamento de modelos e previsão de sentimentos.

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

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
    └── training_pipeline.py
```

- **config:** Contém arquivos de configuração para o projeto.
- **data:** Contém os dados usados no projeto.
- **experiments:** Contém resultados e registros de experimentos.
- **preprocessing:** Contém scripts para pré-processamento de dados.
- **saved models:** Contém modelos treinados salvos.

## Funcionalidades Principais

- **pipeline.py:** Implementa o pipeline principal do projeto.
- **predict.py:** Implementa a funcionalidade de previsão.
- **training_pipeline.py:** Implementa o pipeline de treinamento do modelo.

## Setup

Para configurar o projeto, execute os seguintes comandos:

```bash
python setup.py sdist bdist_wheel
pip install -e .
```