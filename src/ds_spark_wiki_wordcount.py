#import os
#import sys
import matplotlib.pyplot as plt

# os.environ["SPARK_HOME"]="C:/Users/400T6B/Code/s_201111215/spark-2.0.0-bin-hadoop2.6"
# os.environ["PYLIB"]=os.path.join(os.environ["SPARK_HOME"],'python','lib')
# sys.path.insert(0,os.path.join(os.environ["PYLIB"],'py4j-0.10.1-src.zip'))
# sys.path.insert(0,os.path.join(os.environ["PYLIB"],'pyspark.zip'))


import pyspark


def doIt():
    my_Rdd=spark.sparkContext.textFile(os.path.join("data","ds_spark_wiki2.txt"))
    #print my_Rdd.first()

    my_words = my_Rdd.map(lambda x:x.split(' '))

    #my_words2.count()

    #my_words.take(5)

    my_Rdd1 = my_Rdd.map(lambda x:x.replace(",",""))
    my_Rdd2 = my_Rdd1.map(lambda x:x.replace(".",""))

    #word_count = my_Rdd2.flatMap(lambda x:x.split( )).map(lambda x:(x,1)).groupByKey().mapValues(sum).sortByKey(True).take(200)

    #for word in word_count:
    #    print word

    word_count2 = my_Rdd2.flatMap(lambda x:x.split()).map(lambda x:(x,1)).reduceByKey(lambda x,y:x+y).map(lambda x:(x[1],x[0])).sortByKey(False).take(200)

    for word2 in word_count2:
        print word2

    count = map(lambda x:x[0], word_count2) # x
    words = map(lambda x:x[1], word_count2) # y
    plt.barh(range(len(count)), count, color = 'red')
    plt.yticks(range(len(count)), words)
    plt.show()
    
if __name__ == "__main__":    
    myConf=pyspark.SparkConf()
    spark = pyspark.sql.SparkSession.builder\
        .master("local")\
        .appName("myApp")\
        .config(conf=myConf)\
        .config('spark.sql.warehouse.dir', 'file:///C:/Users/400T6B/Code/s_201111215/data')\
        .getOrCreate()
    doIt()
    spark.stop()