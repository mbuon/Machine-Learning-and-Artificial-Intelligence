# for jupyter with LIVY, sparkmagic
# https://github.com/jupyter-incubator/sparkmagic/blob/master/examples/Pyspark%20Kernel.ipynb
from pyspark.sql.types import *

# Generate  data 
ListRDD = sc.parallelize([
    (123, 'Skye', 19, 'brown'),
    (223, 'Rachel', 22, 'green'),
    (333, 'Albert', 23, 'blue') 
    ])

schema = StructType([ StructField("id", LongType(), True), StructField("name", StringType(), True), StructField("age", LongType(), True), StructField("eyeColor", StringType(), True) ])

drivers = spark.createDataFrame(ListRDD, schema)
drivers.createOrReplaceTempView("drivers")