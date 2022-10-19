from datetime import datetime
from airflow.decorators import dag, task, task_group
from airflow.operators.bash import BashOperator
from airflow.operators.python_operator import BranchPythonOperator
import pandas as pd

from scripts.iris_preprocessing import IrisPreprocessing

path_iris = '/mnt/Dados/Documents/GitHub/mlops/trabalho_01/iris_tratado.parquet'
path_scripts = '/mnt/Dados/Documents/GitHub/mlops/trabalho_02/dags/scripts/'

# Definindo alguns argumentos básicos
default_args = {
   'owner': 'admin',
   'depends_on_past': False,
   'start_date': datetime(2019, 1, 1),
   'retries': 0
   }


@dag(default_args=default_args, schedule_interval='*/2 * * * *', description='dag-pipeline-iris-trabalho-02', catchup=False, tags=['iris','mlflow'])
def dag_pipeline_iris_trabalho_02():
        
    @task
    def start():

        return True


    def etl_iris():
        dados = pd.read_parquet(path_iris)
        etl = IrisPreprocessing(dados)
        errors = etl._get_errors()
        if len(errors) > 0:
            print('Dataset possui erros de validação.')

            return 'erro_etl'

        return ['modelos.modelo_01', 'modelos.modelo_02']


    etl = BranchPythonOperator(
    task_id='etl',
    python_callable=etl_iris
    )


    @task_group(group_id='modelos')
    def modelos():
        modelo_01 = BashOperator(
            task_id='modelo_01',
            bash_command=f'''
            cd {path_scripts}
            python modelo_01.py
            ''')


        modelo_02 = BashOperator(
            task_id='modelo_02',
            bash_command=f'''
            cd {path_scripts}
            python modelo_02.py
            ''')

        
        [modelo_01, modelo_02]


    @task
    def erro_etl():
        print('Modelos não executados devido a erros de validação no dataset')

        return False


    @task(trigger_rule='one_success')
    def end():

        return True


    # Orquestração
    start = start()
    erro_etl = erro_etl()
    modelos = modelos()
    end = end()

    start >> etl >> [modelos, erro_etl] >> end

execucao = dag_pipeline_iris_trabalho_02()

# Para executar o DAG no Airflow, basta executar o comando abaixo:
# airflow dags backfill -s 2021-04-02 dag_pipeline_iris_trabalho_02