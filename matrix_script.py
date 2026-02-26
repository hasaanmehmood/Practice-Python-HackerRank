#!/bin/python3

import math
import os
import random
import re
import sys

import re

n, m = map(int, input().split())
matrix = [input() for _ in range(n)]

# 1) Read column-wise
s = ''.join(matrix[i][j] for j in range(m) for i in range(n))

# 2) Replace symbol-runs between alphanumerics with a space
s = re.sub(r'([A-Za-z0-9])[^A-Za-z0-9]+([A-Za-z0-9])', r'\1 \2', s)

print(s)


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
