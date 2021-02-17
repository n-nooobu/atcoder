import io
import sys

# input here
_INPUT = """\
8
-406 10
512 859
494 362
-955 -475
128 553
-986 -885
763 77
449 310

"""
sys.stdin = io.StringIO(_INPUT)



import itertools

N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]

S = 0
p = 0
for i in itertools.permutations([i for i in range(N)]):
    p += 1
    for j in range(1, len(i)):
        S += ((xy[i[j-1]][0] - xy[i[j]][0]) ** 2 + (xy[i[j-1]][1] - xy[i[j]][1]) ** 2) ** 0.5

print(S / p)
