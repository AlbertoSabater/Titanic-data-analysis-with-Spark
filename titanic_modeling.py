# In order to run this as a script using spark-submit,
# the spark context has to be defined
from pyspark import SparkContext, SparkConf
from pyspark.sql import HiveContext
from pyspark.sql import functions as F
from pyspark.sql import SQLContext
from pyspark.ml.feature import StringIndexer
from pyspark.mllib.regression import LabeledPoint
from pyspark.sql.functions import col
from pyspark.ml.feature import VectorAssembler
from pyspark.mllib.tree import GradientBoostedTrees, GradientBoostedTreesModel
#from pyspark.mllib.util import MLUtils


def getError(labels, predictions):
	pairs = labels.zip(predictions)
	error = pairs.filter(lambda l: l[0] == l[1]).count() / float(pairs.count())
	return error

sc = SparkContext()
hive_context = HiveContext(sc)
sqlContext = SQLContext(sc)
sc.setLogLevel("WARN")

data = hive_context.read.table("titanic_train")
data = data.select('survived', 'class', 'sex', 'age', 'sibsip', 'parch', 'fare', 'embarked')
data= data.na.drop()

data = data.withColumn('sex', F.when(data.sex =="male",0).otherwise(1))

indexer = StringIndexer(inputCol='embarked', outputCol='embarkedNum')
data=indexer.fit(data).transform(data)
data = data.drop('embarked')


assembler = VectorAssembler(
    inputCols=["class", "sex", "age","sibsip", "parch", "fare","embarkedNum"],
    outputCol="features")

data = assembler.transform(data)

trainRDD = data.select(col("survived").alias("label"), col("features")).rdd.map(lambda row: LabeledPoint(row.label, row.features))

model = GradientBoostedTrees.trainClassifier(trainRDD, categoricalFeaturesInfo={}, numIterations=15)
predictions = model.predict(trainRDD.map(lambda l: l.features))

print('Train error: ' + str(getError(trainRDD.map(lambda l: l.label), predictions)))


