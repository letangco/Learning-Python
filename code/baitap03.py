from __future__ import print_function
import sys
from operator import add
from pyspark.sql import SparkSession
def toF(strF):
    strNum = strF.split(" ")
    return [int(strNum[0]), int(strNum[1])]
def standardF(f):
    newF = [f[0], 1]
    if (f[1] != 1):
        if (f[1] == 0):
            newF = [0, 1]
        else:
            newF[1] = f[1]
    return newF
def sumF(f1, f2):
    return [f1[0] * f2[1] + f2[0] * f1[1], f1[1] * f2[1]]
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Start: run <file>", file=sys.stderr)
        sys.exit(-1)
    spark = SparkSession\
        .builder\
        .appName("Run")\
        .getOrCreate()

    lines = spark.read.text(sys.argv[1]).rdd.map(lambda r: r[0])
    fractions = [standardF(toF(x)) for x in lines]
    sumOfF = [0, 1] 
    for f in fractions: 
        sumOfF = sumF(sumOfF, f) 
    print("%f %f : %f" % (sumOfF[0], sumOfF[1], sumOfF[0] / sumOfF[1]))
    spark.stop()