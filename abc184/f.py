import io
import sys

# input here
_INPUT = """\
6 100
1 2 7 5 8 10


"""
sys.stdin = io.StringIO(_INPUT)



from bisect import *

N, T = map(int, input().split())
A = list(map(int, input().split()))

L = [0]
R = [0]
for x in A[:N // 2]:
    for i in range(len(L)):
        L.append(x + L[i])
for x in A[N // 2:]:
    for i in range(len(R)):
        R.append(x + R[i])
R = sorted(R)

ans = 0
for i in range(len(L)):
    if L[i] > T:
        continue
    t = L[i] + R[bisect_right(R, T - L[i]) - 1]
    ans = max(ans, t)

print(ans)
