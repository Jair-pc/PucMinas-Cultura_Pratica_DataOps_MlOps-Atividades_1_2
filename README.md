#### PÓS GRADUAÇÃO ENGENHERIA DE DADOS PUC MINAS

# Cultura e Práticas Dataops e Mlops

## Atividades

## Atividade 1

**Objetivo:** ETL utilizando o Pyspark .

## Etapas a serem desenvolvidas:

1 - Download do arquivo: https://drive.google.com/file/d/1rZgVuwYon_3QogTr0-v480PRpi-2l1-v/view?usp=sharingLinks para um site externo.   

2 - Criar uma task pre-processamento para validar se os dados se encontram no formato correto utilizando Pyspark:   

 * sepal_length range( 4.3,7.9)  
 * sepal_width range(2.0,4.4)  
 * petal_length range(1.0,6.9)  
 * petal_width range(0.1,2.5)   
 * classEncoder range(0,2)   
 * class ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']   
     
4 - Utilizar a lib pydeequ para gerar o data quality report. (Gerar o report após a leitura do arquivo e após ter realizado o tratamento dos dados.)

5 - Criar dataset tratado no formato parquet.    

**OBS:** Todos os dados que não se encontram no formato ou range correto devem ser excluídos do dataset.   

**OBS2:** Criar um arquivo com os registros removidos contendo a mensagem do erro conforme exemplo:   

1 - sepal_length,sepal_width,petal_length,petal_width,class,classEncoder,messageError

2 - 5.1,3.5,1.4,0.2,Iris-setosa,0, sepal_width maior que 4.4    

- [Atividade 01](./Trabalho_01/)  


## Atividade 2   

**Objetivo:** Orquestrar todo o fluxo de processamento necessários para execução de um modelo de machine learning utilizando o airflow.   

## Etapas a serem desenvolvidas:   

1 - Criar uma task etl responsável pela leitura do arquivo Iris tratado (Atividade 01) e utilize a lib pandas-schema para verificar se os dados estão no formato correto. Se o arquivo estiver correto continuar para a próxima task e em caso de erro pausar o processamento e enviar mensagem de erro.   
 
 * sepal_length range(4.3,7.9)    
 * sepal_width range(2.0,4.4)     
 * petal_length range(1.0,6.9)   
 * petal_width range(0.1,2.5)    
 * classEncoder range(0,2)   
 * class ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']   
   
2 - Criar uma task de grupo que contenha: 

* Execução algoritmo1 de ML para o dataset Iris
* 
* Execução algoritmo2 de ML para o dataset Iris
* 
      OBS: O processamento deve ser realizado de forma paralela

      OBS2: Utilizar o MLFlow para gerenciar os modelos criados

- [Atividade 02](./Trabalho_02/)
