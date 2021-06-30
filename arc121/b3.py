import io
import sys

# input here
_INPUT = """\
4
5 R
2 R
3 R
10 G
11 G
12 G
1 B
10 B
"""
sys.stdin = io.StringIO(_INPUT)



import math
from bisect import *

N = int(input())

color2id = {'R': 0, 'G': 1, 'B': 2}
AC = [[] for _ in range(3)]
for i in range(2 * N):
    a, c = input().split()
    AC[color2id[c]].append(int(a))
for i in range(3):
    AC[i] = sorted(AC[i])
is_odd = [len(AC[i]) % 2 for i in range(3)]

def cal_min_pair(l0, l1):
    mi = math.inf
    for a in l0:
        if bisect_left(l1, a) > 0:
            mi = min(mi, abs(a - l1[bisect_left(l1, a) - 1]))
        if bisect_left(l1, a) < len(l1):
            mi = min(mi, abs(a - l1[bisect_left(l1, a)]))
    return mi

if sum(is_odd) == 0:
    print(0)
else:
    tar = [0] * 3
    cnt = 0
    for i in range(3):
        if is_odd[i] == 0:
            tar[2] = i
        elif cnt == 0:
            tar[0] = i
            cnt += 1
        else:
            tar[1] = i

    mi1 = cal_min_pair(AC[tar[0]], AC[tar[1]])
    mi2 = cal_min_pair(AC[tar[0]], AC[tar[2]])
    mi3 = cal_min_pair(AC[tar[1]], AC[tar[2]])

    print(min(mi1, mi2 + mi3))
