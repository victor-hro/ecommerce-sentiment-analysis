import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from pipeline import nlp_pipeline
from config import config
from preprocessing import data_handling
import time
import os

def main():
    # Configuração da página
    st.set_page_config(
        page_title="Análise de Sentimentos",
        page_icon=":chart_with_upwards_trend:",
    )

    # Título da página
    st.title("O que você achou do nosso produto?")
    st.write('--'*10)

    # Campo de entrada para o nome do produto
    st.chat_message('user').write("Qual produto você comprou?")
    product_input = st.text_input("Digite aqui o nome do produto")

    # Campo de entrada para o comentário do usuário
    st.chat_message('user').write("O que você achou do nosso produto?")
    user_input = st.text_area("Deixe seu comentário aqui:")

    # Botão para enviar os dados
    if st.button("Enviar Dados"):
        # Criar um DataFrame com os dados inseridos pelo usuário
        df = pd.DataFrame({
            'product': [product_input],
            'review_comment_message': [user_input]
        })

        # Carregar o modelo de análise de sentimento
        model = data_handling.load_pipeline()
        
        # Realizar a previsão do sentimento do comentário do usuário
        X = model.predict(df['review_comment_message'])
        df['predict'] = X
        
        # Salvar os dados no arquivo de saída
        df.to_csv(config.SITE_OUTPUT_DATASET,
                  mode='a',
                  header=not os.path.exists(config.SITE_OUTPUT_DATASET),
                  index=None)

        # Exibir mensagem de sucesso
        st.write("Dados enviados com sucesso!")
        st.write('--'*10)
        st.write("Desenvolvido por Victor Oliveira")

if __name__ == "__main__":
    # Função principal
    main()

    # Aguardar 2 segundos para carregar os dados
    time.sleep(2)
    
    # Carregar os dados do arquivo de saída
    df_predictions = data_handling.load_data(filepath=config.SITE_OUTPUT_DATASET)

    # Contar o número de avaliações positivas para cada produto
    top_products = (
        df_predictions[df_predictions['predict'] == 1]
        .groupby('product')
        .size()
        .sort_values(ascending=False)
        .head(5)
        .to_frame()
        .reset_index()
    )

    # Mapeamento de ícones para cada categoria
    icons = {
        1: "🥇",
        2: "🥈",
        3: "🥉"
    }

    # Exibir os 3 principais produtos com avaliações positivas
    c1, c2, c3 = st.columns(3)
    with c1:
        st.info(f"{icons.get(1)} 1: {top_products['product'][0]}")

    with c2:
        st.info(f"{icons.get(2)} 2: {top_products['product'][1]}")

    with c3:
        st.info(f"{icons.get(3)} 3: {top_products['product'][2]}")

    # Criar a nuvem de palavras com os comentários dos usuários
    st.subheader("Veja o que as pessoas estão falando:")
    wordcloud = WordCloud(width=700, height=300, background_color='black').generate(' '.join(df_predictions['review_comment_message']))

    # Exibir a nuvem de palavras
    st.image(wordcloud.to_array(), use_column_width=False)
