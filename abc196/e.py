import io
import sys

# input here
_INPUT = """\
3
-10 2
10 1
-5 3
5
-15 -10 -5 0 5

"""
sys.stdin = io.StringIO(_INPUT)



import math

N = int(input())

f = [-math.inf, 0, math.inf]
flag = False
for i in range(N):
    a, t = map(int, input().split())
    if t == 1:
        if not flag:
            for j in range(3):
                f[j] += a
        else:
            f += a
    elif t == 2:
        if not flag:
            if a >= f[2]:
                flag = True
                f = a
            else:
                f[0] = max(f[0], a)
        else:
            f = max(f, a)
    else:
        if not flag:
            if a <= f[0]:
                flag = True
                f = a
            else:
                f[2] = min(f[2], a)
        else:
            f = min(f, a)

Q = int(input())
x = list(map(int, input().split()))

for i in range(Q):
    if flag:
        print(f)
    else:
        if x[i] <= f[0] - f[1]:
            print(f[0])
        elif x[i] >= f[2] - f[1]:
            print(f[2])
        else:
            print(x[i] + f[1])
