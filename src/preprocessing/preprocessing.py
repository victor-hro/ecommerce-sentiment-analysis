import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer
from sklearn.base import BaseEstimator, TransformerMixin
import string
import nltk

nltk.download('punkt')
nltk.download('stopwords')

class DataPreprocessing(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.stemmer = SnowballStemmer('portuguese')
        self.stop_words = set(stopwords.words('portuguese'))

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X_processed = []
        for text in X:
            cleaned_text = self.clean_text(text)
            tokenized_text = self.tokenize_data(cleaned_text)
            without_stopwords = self.remove_stopwords(tokenized_text)
            stemmed_text = self.stemming_process(without_stopwords)
            X_processed.append(' '.join(stemmed_text))
        return X_processed

    def clean_text(self, text):
        text = text.lower()  # Converter para minúsculas
        text = text.translate(str.maketrans('', '', string.punctuation))  # Remover pontuações
        text = ' '.join([word for word in text.split() if not any(c.isdigit() for c in word)])  # Remover números
        return text

    def tokenize_data(self, text):
        return word_tokenize(text)

    def remove_stopwords(self, text):
        return [word for word in text if word not in self.stop_words]

    def stemming_process(self, text):
        return [self.stemmer.stem(word) for word in text]
