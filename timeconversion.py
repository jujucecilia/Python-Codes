import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    if s[-2:] == "AM" and s[:2] =="12":
        return '00' + s[2:-2]
        
    elif s[-2:] == "AM":
        return S[:-2]
        
    elif s[-2:] == "PM" and s[:2]=="12":
        return s[:-2]
    else:
        return str(int(s[:2])+12)+s[2:8]

s = input("Input time (Format: XX:XX:XX PM): ")
print(timeConversion())


