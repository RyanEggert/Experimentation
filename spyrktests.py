# spyrktests.py

from spyrk import SparkCloud
from spyrk_config import authentication
from time import sleep

spark = SparkCloud(authentication['accesstoken'])

print spark.devices     # List all avaliable spark cores (dictionary with names). We have one. 

print spark.RE_core1.variables  # Dictionary of all exposed variable (names) and their types

print spark.RE_core1.testinteger
print spark.RE_core1.testString.encode('utf-8')


for i in xrange(1000):
    # print spark.RE_core1.blink
    print spark.RE_core1.analogRead()

