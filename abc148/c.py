import io
import sys

# input here
_INPUT = """\
100000 99999

"""
sys.stdin = io.StringIO(_INPUT)



import math

A, B = map(int, input().split())

print(int(A / math.gcd(A, B) * B))
