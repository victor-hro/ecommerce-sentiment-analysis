from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import LogisticRegression
from preprocessing.preprocessing import DataPreprocessing
from config import config


model_params = {
    'max_iter': 100000
    , 'solver': 'lbfgs'
    , 'random_state': config.SEED
}

nlp_pipeline = Pipeline([
    ('preprocessing', DataPreprocessing()),
    ('vectorizer', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('model', LogisticRegression(**model_params))
])