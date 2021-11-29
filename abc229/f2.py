import io
import sys

# input here
_INPUT = """\
4
100 100 100 1000000000
1 2 3 4

"""
sys.stdin = io.StringIO(_INPUT)



import math

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [[[math.inf] * 2 for j in range(2)] for i in range(N)]

