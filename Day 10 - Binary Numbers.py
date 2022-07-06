#!/bin/python3

import math
import os
import random
import re
import sys

def binary(n):
    biner = '0'
    maks = 1
    consecutive = 1
    while n > 0:
        if biner[-1] == '1' and n%2 == 1:
            consecutive += 1
        else:
            if consecutive > maks:
                maks = consecutive
            consecutive = 1
        biner += str(n%2)
        n = n // 2
        if n == 0:
            if consecutive > maks:
                maks = consecutive
    return(maks)

if __name__ == '__main__':
    n = int(input().strip())
    print(binary(n))