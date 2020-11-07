import io
import sys

# input here
_INPUT = """\
4 6
67786 3
1 3 4
3497 1
2
44908 3
2 3 4
2156 3
2 3 4
26230 1
2
86918 1
3


"""
sys.stdin = io.StringIO(_INPUT)



N, M = map(int, input().split())
a = []
b = []
c = []
for _ in range(M):
    ta, tb = map(int, input().split())
    a.append(ta)
    b.append(tb)
    c.append(list(map(int, input().split())))

INF = 10 ** 8
dp = [INF] * 2 ** N
dp[0] = 0
for i in range(len(dp)):
    for j in range(M):
        state = 0
        for k in range(b[j]):
            state += 2 ** (c[j][k] - 1)
        dp[i | state] = min(dp[i | state], dp[i] + a[j])

if dp[-1] != INF:
    print(dp[-1])
else:
    print(-1)
