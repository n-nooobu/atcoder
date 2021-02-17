import io
import sys

# input here
_INPUT = """\
1
"""
sys.stdin = io.StringIO(_INPUT)



import math

N = int(input())

s = 1
for i in range(2, math.floor(math.sqrt(N)) + 1):
    if N % i == 0:
        s += i
        if N // i != i:
            s += N // i

if N == 1:
    print('Deficient')
elif s == N:
    print('Perfect')
elif s < N:
    print('Deficient')
else:
    print('Abundant')
