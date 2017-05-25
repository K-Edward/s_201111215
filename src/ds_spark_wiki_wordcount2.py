
import os
from operator import add
import pyspark
from pyspark.mllib.feature import HashingTF

def doIt2():    
    #word_count = spark.sparkContext.textFile(os.path.join("data","ds_spark_wiki2.txt")).flatMap(lambda x: x.split(' ')).map(lambda x: (x.lower().rstrip().lstrip().rstrip(',').rstrip('.'), 1)).reduceByKey(add)
    word_count = spark.sparkContext.textFile(os.path.join("data","ds_spark_wiki2.txt")).map(lambda x: x.replace('.',' ').replace(',',' ').replace('/',' ').replace('-',' ').replace('"',' ').replace('(',' ').replace(')',' ').lower()).map(lambda x:x.split()).map(lambda x:[(i,1) for i in x])
    documents = spark.sparkContext.textFile(os.path.join("data","ds_spark_wiki2.txt")).map(lambda x: x.split(" "))
    h_TF = HashingTF()
    tf = h_TF.transform(documents)
    tf.collect()

if __name__ == "__main__":
    myConf=pyspark.SparkConf()
    spark = pyspark.sql.SparkSession.builder\
        .master("local")\
        .appName("myApp")\
        .config(conf=myConf)\
        .config('spark.sql.warehouse.dir', 'file:///C:/Users/88/Code/s_201111215/data')\
        .getOrCreate()
    doIt2()
    spark.stop()