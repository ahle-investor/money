import sys
# import numpy as np
# import pandas as pd
# from sklearn import ...
def convert_string(my_str):
    return ' '.join(s[0]+s[1:] for s in my_str.split())

for line in sys.stdin.split("\n"):
    print(line, end="\n")
    