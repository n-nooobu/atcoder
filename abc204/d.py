import io
import sys

# input here
_INPUT = """\
9
3 14 15 9 26 5 35 89 79

"""
sys.stdin = io.StringIO(_INPUT)



import math
from copy import copy

N = int(input())
T = sorted(list(map(int, input().split())), reverse=True)
Tsum = sum(T)

s = set()
for i in range(N):
    s2 = copy(s)
    for j in s:
        s2.add(j + T[i])
    s2.add(T[i])
    s = s2

ans = math.inf
for i in s:
    ans = min(ans, max(i, Tsum - i))

print(ans)
