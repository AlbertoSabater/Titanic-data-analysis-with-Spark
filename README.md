# Titanic: Machine Learning from Disaster

This is the code for the Kaggle competition with  the Titanic data.
https://www.kaggle.com/c/titanic

This code runs on Spark with python using Data Frames and RDDs to work with the data.
The needed data is located in the Kaggle's web.
https://www.kaggle.com/c/titanic/data


Before running the script, the data is needed to be stored in hdfs:
hdfs dfs -mkdir /titanic
hdfs dfs -put *.csv /titanic

Then is needed to create two Hive tables to access easily to this data:
hive -f hive_tables.hql

Finally, run the script to train and test a model to predict the Titanic's survivors:
spark-submit titanic_modeling.py


