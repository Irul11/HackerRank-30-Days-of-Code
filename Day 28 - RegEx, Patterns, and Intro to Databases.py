import math
import os
import random
import re
import sys

N = int(input().strip())

regex = r'([a-z]{1,20})\s([a-z\.]{1,40}@gmail.com)'
regex_name = r'[a-z]'
teks = list()
for N_itr in range(N):
    first_multiple_input = input().rstrip()
    firstName = first_multiple_input.split()[0]
    emailID = first_multiple_input.split()[1]

    if re.match(regex, first_multiple_input):
        teks += [re.match(regex, first_multiple_input).group(1)]

print('\n'.join(sorted(teks)))