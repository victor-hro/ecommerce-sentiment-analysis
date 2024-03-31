import pathlib
import os
import src

SEED = 42

PACKAGE_ROOT = pathlib.Path(src.__file__).resolve().parent

DATAPATH = os.path.join(PACKAGE_ROOT, "data")
TRAINPATH = os.path.join(DATAPATH, 'train.csv')
TESTPATH = os.path.join(DATAPATH, 'test.csv')
MODELPATH = os.path.join(PACKAGE_ROOT, "saved_models")

DATASETPATH = os.path.join(DATAPATH, 'olist_order_reviews_dataset.csv')
MODELFILE = os.path.join(MODELPATH, 'model.joblib')


TRAIN_COLUMNS = ['review_comment_message', 'review_target']
PREDICT_COLUMNS = ['review_comment_message']