import io
import sys

# input here
_INPUT = """\
3 4 3
1 9
5 3
7 8
1 8 6 9
4 4
1 4
1 3


"""
sys.stdin = io.StringIO(_INPUT)



N, M, Q = map(int, input().split())
WV = [list(map(int, input().split())) for _ in range(N)]
WV = sorted(WV, reverse=True, key=lambda x: x[1])
X = list(map(int, input().split()))

for q in range(Q):
    L, R = map(int, input().split())
    x = sorted(X[:L - 1] + X[R:])
    ans = 0
    for w, v in WV:
        for i, a in enumerate(x):
            if w <= a and x[i] > 0:
                ans += v
                x[i] = 0
                break
    print(ans)
