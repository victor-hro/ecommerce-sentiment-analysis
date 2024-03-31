import pandas as pd
from config import config
import joblib

# Load the dataset
def load_data(filepath: str=config.DATASETPATH):
    df = pd.read_csv(filepath)
    df = (
        df.dropna(subset=['review_comment_message'])
        .reset_index(drop=True)
        )
    print('Data loaded')
    return df

# Save the dataset
def save_data(df, filepath: str):
    df.to_csv(filepath, index=None)
    print(f'Data saved: {filepath}')
    return


# Serialization
def save_pipeline(pipeline, filepath: str=config.MODELFILE):
    joblib.dump(pipeline, filepath)
    print(f"Model has been saved: {config.MODELFILE}")
    
# Deserialization
def load_pipeline(filepath: str=config.MODELFILE):
    model = joblib.load(filepath)
    print(f"Model has been loaded")
    return model