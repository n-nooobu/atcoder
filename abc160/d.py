import io
import sys

# input here
_INPUT = """\
10 4 8

"""
sys.stdin = io.StringIO(_INPUT)



N, X, Y = map(int, input().split())

ans = [0] * N
for i in range(1, N):
    for j in range(i + 1, N + 1):
        if j <= X:
            ans[j - i] += 1
        else:
            ans[min(j - i, max(j - Y, Y - j) + 1 + max(i - X, X - i))] += 1

for i in range(1, N):
    print(ans[i])
