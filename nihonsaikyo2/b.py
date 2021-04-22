import io
import sys

# input here
_INPUT = """\
4 4
1 2 3 4
1 2 3 4

"""
sys.stdin = io.StringIO(_INPUT)



N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a = max(A)
b = max(B)
seena = [False] * (max(a, b) + 1)
seenb = [False] * (max(a, b) + 1)
for i in range(N):
    seena[A[i]] = True
for i in range(M):
    seenb[B[i]] = True
ans = []
for i in range(M):
    if seena[B[i]]:
        continue
    ans.append(B[i])
for i in range(N):
    if seenb[A[i]]:
        continue
    ans.append(A[i])
ans = sorted(ans)
for i in ans:
    print(i, end=' ')
