
from sys import argv

import sys
import numpy as np


path = sys.argv[1]
cs = 0
last = 0

with open(path, "rb") as f:
    data = f.read()
    

print(data[1])
print(hex(sum(data[:-1])))