import io
import sys

# input here
_INPUT = """\
20 12
7 11 10 1 7 20 14 2 17 3 2 5 19 20 8 14 18 2 10 10

"""
sys.stdin = io.StringIO(_INPUT)



N, X = map(int, input().split())
A = list(map(int, input().split()))

used = [0] * (N + 1)
used[X] = 1
t = A[X - 1]
ans = 1
while not used[t]:
    ans += 1
    used[t] = 1
    t = A[t - 1]

print(ans)
