import io
import sys

# input here
_INPUT = """\
8
5 7 4 2 6 8 1 3

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
P = list(map(int, input().split()))

m = 10 ** 6
ans = 0
for i in range(N):
    if P[i] <= m:
        ans += 1
        m = P[i]

print(ans)
