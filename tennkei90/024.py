import io
import sys

# input here
_INPUT = """\
7 999999999
3 1 4 1 5 9 2
1 2 3 4 5 6 7

"""
sys.stdin = io.StringIO(_INPUT)



N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

d = 0
for i in range(N):
    d += abs(A[i] - B[i])

if d > K:
    print('No')
else:
    if (K - d) % 2 == 0:
        print('Yes')
    else:
        print('No')
