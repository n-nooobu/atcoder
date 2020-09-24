import io
import sys

# input here
_INPUT = """\
32
3 1 4 1 5 9 2 6 5 3 5 8 9 7 9 3 2 3 8 4 6 2 6 4 3 3 8 3 2 7 9 5
"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
A = list(map(int, input().split()))

t = [0] * (N + 1)
ans = 0
for i in range(N):
    sa = i - A[i]
    if sa >= 0:
        ans += t[sa]
    wa = i + A[i]
    if wa < N:
        t[wa] += 1

print(ans)
