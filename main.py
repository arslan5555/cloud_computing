import re
import json
import glob
import os
import operator
from collections import Counter

from my_function import file_function

#b = dict( han = 0, hon = 0, den = 0, det = 0, denna = 0, denne=0, hen=0)
A = Counter({'han' : 0, 'hon' : 0, 'den' : 0, 'det' : 0, 'denna' : 0, 'denne': 0, 'hen' : 0})

path = "/home/ubuntu/data"
dir_list = os.listdir(path)

for name in dir_list:
	a=file_function(name)
	A= a + A
print(A)
