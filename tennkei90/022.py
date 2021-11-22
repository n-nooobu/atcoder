import io
import sys

# input here
_INPUT = """\
1000000000000000000 999999999999999999 999999999999999998

"""
sys.stdin = io.StringIO(_INPUT)



import math

A, B, C = map(int, input().split())

e = math.gcd(math.gcd(A, B), C)
print(A // e + B // e + C // e - 3)
