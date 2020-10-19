import io
import sys

# input here
_INPUT = """\
720
"""
sys.stdin = io.StringIO(_INPUT)


import math

N = int(input())

ans = set()
for i in range(1, round(math.sqrt(N)) + 1):
    if N % i == 0:
        ans.add(i)
        ans.add(N // i)

ans = list(sorted(ans))
for i in range(len(ans)):
    print(ans[i])
