import warnings
import os

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import precision_score, accuracy_score, f1_score

import mlflow
import mlflow.sklearn
from urllib.parse import urlparse
import pickle

import logging

logging.basicConfig(level=logging.WARN)
logger = logging.getLogger(__name__)


def eval_metrics(actual, pred):
    precision = precision_score(actual, pred, average='macro')
    accuracy = accuracy_score(actual, pred, normalize=False)
    f1 = f1_score(actual, pred, average='macro')

    return precision, accuracy, f1


warnings.filterwarnings('ignore')
np.random.seed(40)

path_iris = '/mnt/Dados/Documents/GitHub/mlops/trabalho_01/iris_tratado.parquet'
dados = pd.read_parquet(path_iris)

X_train, X_test, y_train, y_test = train_test_split(dados.iloc[:,:4], dados['classEncoder'], random_state=0)

alpha = 0.5
l1_ratio = 0.5


with mlflow.start_run():
        
    mlflow.log_param('alpha', alpha)
    mlflow.log_param('l1_ratio', l1_ratio)
    
    mlp = MLPClassifier()
    mlp.fit(X_train, y_train)
    y_pred = mlp.predict(X_test)

    predicted_qualities = mlp.predict(X_test)

    (precision, accuracy, f1) = eval_metrics(y_test, predicted_qualities)

    print(f'PRECISION: {precision}' )
    print(f'ACCURACY: {accuracy}')
    print(f'F1: {f1}')

    mlflow.log_metric('precision', precision)
    mlflow.log_metric('accuracy', accuracy)
    mlflow.log_metric('f1', f1)

    tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

    ## Salvando Modelo
    file = '/mnt/Dados/Documents/GitHub/mlops/trabalho_02/modelos/mlp.pickle'
    os.makedirs(os.path.dirname(file), exist_ok=True)
    with open('/mnt/Dados/Documents/GitHub/mlops/trabalho_02/modelos/mlp.pickle','wb') as f:
        pickle.dump(mlp, f)

    if tracking_url_type_store != 'file':
        mlflow.sklearn.log_model(mlp, 'model', registered_model_name='model')
    else:
        mlflow.sklearn.log_model(mlp, 'model')

