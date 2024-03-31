from pipeline import nlp_pipeline
import pandas as pd
from config import config
from preprocessing import data_handling

df = data_handling.load_data(config.TESTPATH)
model = data_handling.load_pipeline()

X = model.predict(df['review_comment_message'])
print(X[0:20])