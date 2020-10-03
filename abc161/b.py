import io
import sys

# input here
_INPUT = """\
12 3
4 56 78 901 2 345 67 890 123 45 6 789
"""
sys.stdin = io.StringIO(_INPUT)



N, M = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
for i in range(N):
    if A[i] >= sum(A) / (4 * M):
        ans += 1

if ans >= M:
    print('Yes')
else:
    print('No')
