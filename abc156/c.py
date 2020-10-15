import io
import sys

# input here
_INPUT = """\
7
14 14 2 13 56 2 37


"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
X = list(map(int, input().split()))

P = round(sum(X) / N)
ans = 0
for i in range(N):
    ans += (X[i] - P) ** 2

print(ans)
