from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession

spark_context = SparkContext(master="local",appName="exam")

def odd_even (x):
    if x%2==0:
        x=x*x
    else:
        x=x*x*x
    return x

def cond(x):
    if x>100 and x<500:
        return True
    else:
        return True

myRDD = spark_context.parallelize([1,2,3,4,5,6,7,8,9])
myRDD = myRDD.map(odd_even)
print(myRDD.first())

myRDD =myRDD.filter(cond)
print(myRDD.count())

print(myRDD.collect())

