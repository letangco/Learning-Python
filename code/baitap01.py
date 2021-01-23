from pyspark.sql import SparkSession
from __future__ import print_function
import sys
from operator import add

def TinhTrunBinh(data):
    if (data.__len__() <= 0):
        return 0
    return sum(data) / data.__len__()


def TinhTrungBinhNhan(data):
    if (data.__len__() <= 0):
        return 1
    value = 1
    for x in data:
        value *= x
    return value ** (1 / data.__len__())


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Start: run <file>", file=sys.stderr)
        sys.exit(-1)
    spark = SparkSession.builder.appName("Run").getOrCreate()
    lines = spark.read.text(sys.argv[1]).rdd.map(lambda r: r[0])
    numbers = [float(x) for x in lines]
    print("%f %f" % (TinhTrunBinh(numbers), TinhTrungBinhNhan(numbers)))
    spark.stop()
