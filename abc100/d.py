import io
import sys

# input here
_INPUT = """\
3 2
2000000000 -9000000000 4000000000
7000000000 -5000000000 3000000000
6000000000 -1000000000 8000000000

"""
sys.stdin = io.StringIO(_INPUT)



N, M = map(int, input().split())
X, Y, Z = [], [], []
for _ in range(N):
    x, y, z = map(int, input().split())
    X.append(x)
    Y.append(y)
    Z.append(z)

ans = 0
for a in range(2):
    for b in range(2):
        for c in range(2):
            if a:
                x = [-X[i] for i in range(N)]
            else:
                x = X
            if b:
                y = [-Y[i] for i in range(N)]
            else:
                y = Y
            if c:
                z = [-Z[i] for i in range(N)]
            else:
                z = Z
            s = sorted([x[i] + y[i] + z[i] for i in range(N)], reverse=True)
            ans = max(ans, sum(s[:M]))

print(ans)
