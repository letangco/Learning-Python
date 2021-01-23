from __future__ import print_function
import sys
from operator import add
from pyspark.sql import SparkSession
import math

def TinhTrungBinhDS(data):
    if (data.__len__() <= 0):
        return 0
    return sum(data) / data.__len__()
def XuLyPhuongSai(dataTB):
    if (dataTB.__len__() <= 0):
        return 0
        average = TinhTrungBinhDS(dataTB)
    sumOfDifference = 0
    for x in dataTB:
        sumOfDifference += (x-average)**2
    return sumOfDifference / dataTB.__len__()
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: run <file>", file=sys.stderr)
        sys.exit(-1)
    spark = SparkSession.builder.appName("Run").getOrCreate()  

    lines = spark.read.text(sys.argv[1]).rdd.map(lambda r: r[0])
    numbers = [float(x) for x in lines]
    variance = XuLyPhuongSai(numbers)
    standardDeviation = math.sqrt(variance)
    print("%f %f" % (variance, standardDeviation))
    spark.stop()