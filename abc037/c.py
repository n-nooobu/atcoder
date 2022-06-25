import io
import sys

# input here
_INPUT = """\
20 10
100000000 100000000 98667799 100000000 100000000 100000000 100000000 99986657 100000000 100000000 100000000 100000000 100000000 98995577 100000000 100000000 99999876 100000000 100000000 99999999

"""
sys.stdin = io.StringIO(_INPUT)



N, K = map(int, input().split())
a = list(map(int, input().split()))

c = [0]
for i in range(N):
    c.append(c[-1] + a[i])

ans = 0
for i in range(N - K + 1):
    ans += c[i + K] - c[i]

print(ans)
