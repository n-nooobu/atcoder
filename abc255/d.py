import io
import sys

# input here
_INPUT = """\
10 5
1000000000 314159265 271828182 141421356 161803398 0 777777777 255255255 536870912 998244353
555555555
321654987
1000000000
789456123
0

"""
sys.stdin = io.StringIO(_INPUT)



from bisect import *

N, Q = map(int, input().split())
A = sorted(list(map(int, input().split())))

A_left = [0] * N
A_left[0] = A[-1] - A[0]
for i in range(1, N):
    A_left[i] = A_left[i - 1] + A[-1] - A[i]
A_right = [0] * N
A_right[N - 1] = A[-1] - A[0]
for i in range(N - 2, -1, -1):
    A_right[i] = A_right[i + 1] + A[i] - A[0]

for q in range(Q):
    X = int(input())

    ans = 0
    index = bisect_left(A, X)

    if index > 0:
        ans += A_left[index - 1] - (A[-1] - X) * index
    if index < N:
        ans += A_right[index] - (X - A[0]) * (N - index)

    print(ans)
