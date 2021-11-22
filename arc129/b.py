import io
import sys

# input here
_INPUT = """\
10
64 96
30 78
52 61
18 28
9 34
42 86
11 49
1 79
13 59
70 95

"""
sys.stdin = io.StringIO(_INPUT)



import math

N = int(input())
LR = [list(map(int, input().split())) for _ in range(N)]

A = [LR[0][0]]
B = [LR[0][1]]
for i in range(1, N):
    A.append(max(A[-1], LR[i][0]))
    B.append(min(B[-1], LR[i][1]))

for i in range(N):
    if A[i] <= B[i]:
        print(0)
    else:
        print(math.ceil((A[i] - B[i]) / 2))
