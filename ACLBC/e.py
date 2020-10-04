import io
import sys

# input here
_INPUT = """\
8 5
3 6 2
1 4 7
3 8 3
2 2 2
4 5 1
"""
sys.stdin = io.StringIO(_INPUT)



N, Q = map(int, input().split())
LRD = [list(map(int, input().split())) for _ in range(Q)]

mod = 998244353

l = []
t = ''
for i in range(100000):
    t += '1'
for i in range(1, 10):
    l.append(str(int(t) * i))

S = ''
for i in range(N):
    S += '1'

for i in range(Q):
    t = l[LRD[i][2] - 1]
    while len(t) < LRD[i][1] - LRD[i][0] + 1:
        t += t
    S = S[:LRD[i][0] - 1] + t[:LRD[i][1] - LRD[i][0] + 1] + S[LRD[i][1]:]
    print(int(S) % mod)
