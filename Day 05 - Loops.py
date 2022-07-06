import math
import os
import random
import re
import sys

def mult(n):
    teks = ''
    for i in range(1,11):
        teks += '{} x {} = {}\n'.format(n, i, n*i)
    return teks

if __name__ == '__main__':
    n = int(input().strip())
    print(mult(n))