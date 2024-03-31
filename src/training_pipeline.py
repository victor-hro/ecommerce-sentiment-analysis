import pandas as pd
import pipeline as pipe
from preprocessing.data_handling import load_data, save_pipeline
import pipeline as pipe
from config import config
import joblib

from sklearn.model_selection import train_test_split


def perform_training():
    train_data = load_data(config.DATASETPATH)

    # selecionando colunas
    df_reviews = train_data[['review_score', 'review_comment_message']].copy()

    # dropando nulos e resetando o index
    df_reviews = (
        df_reviews.dropna(subset=['review_comment_message'])
        .reset_index(drop=True)
        )
    
    classification = lambda x: 1 if x > 3 else 0
    df_reviews['review_target'] = df_reviews['review_score'].apply(classification)

    
    X_train, X_test, y_train, y_test = train_test_split(df_reviews['review_comment_message']
                                                        , df_reviews['review_target']
                                                        , test_size=0.2
                                                        , random_state=config.SEED)

        
    pipe.nlp_pipeline.fit(X_train, y_train)
    save_pipeline(pipe.nlp_pipeline, config.MODELFILE)

if __name__=='__main__':
    perform_training()