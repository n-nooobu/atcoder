import io
import sys

# input here
_INPUT = """\
10
3 -1 -4 1 -5 9 2 -6 5 -3

"""
sys.stdin = io.StringIO(_INPUT)



import math

N = int(input())
x = list(map(int, input().split()))

ans = 0
for i in range(N):
    ans += abs(x[i])
print(ans)

ans = 0
for i in range(N):
    ans += abs(x[i]) ** 2
print(math.sqrt(ans))

ans = 0
for i in range(N):
    ans = max(ans, abs(x[i]))
print(ans)
