import io
import sys

# input here
_INPUT = """\
3
1 -1
-1 4
-1 6
"""
sys.stdin = io.StringIO(_INPUT)



import sys

N = int(input())
A = []
B = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    A.append(tmp[0])
    B.append(tmp[1])

e = [[0] * N for _ in range(2 * N)]
for i in range(N):
    if A[i] > 0:
        e[A[i] - 1][i] = 1
    if B[i] > 0:
        e[B[i] - 1][i] = 1

for i in range(2 * N):
    if sum(e[i]) > 1:
        print('No')
        sys.exit()

for i in range(N):
    if B[i] - A[i] > N:
        print('No')
        sys.exit()


