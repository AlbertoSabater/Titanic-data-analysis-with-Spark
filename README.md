# Titanic-data-analysis-with-Spark

hdfs dfs -mkdir /titanic
hdfs dfs -put *.csv /titanic

hive -f hive_tables.hql


spark-submit titanic_modeling.py


