import io
import sys

# input here
_INPUT = """\
5
-5 8 9 -4 -3

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
A = list(map(int, input().split()))

s = sum(A)
Aij = 0
A2 = 0
for i in range(N - 1):
    s -= A[i]
    Aij += s * A[i]
    A2 += A[i] ** 2
A2 += A[-1] ** 2

print(A2 * (N - 1) - 2 * Aij)
