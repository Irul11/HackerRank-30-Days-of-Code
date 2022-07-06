# 06-11-2022

#!/bin/python3

import math
import os
import random
import re
import sys

def total_cost(price, tip, tax):
    result = price + price*tip/100 + price*tax/100
    teks = '{:.0f}'.format(result)
    return teks

if __name__ == '__main__':
    price = float(input())
    tip = int(input())
    tax = int(input())
    print(total_cost(price, tip, tax))

