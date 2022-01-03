import io
import sys

# input here
_INPUT = """\
5 3 2
1 5 1 5

"""
sys.stdin = io.StringIO(_INPUT)



N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())

ans = [['.'] * (S - R + 1) for _ in range(Q - P + 1)]
for i in range(P, Q + 1):
    for j in range(R, S + 1):
        ki = i - A
        kj0 = j - B
        kj1 = B - j
        if ki == kj0 and max(1 - A, 1 - B) <= ki <= min(N - A, N - B):
            ans[i - P][j - R] = '#'
        if ki == kj1 and max(1 - A, B - N) <= ki <= min(N - A, B - 1):
            ans[i - P][j - R] = '#'

for i in range(Q - P + 1):
    print(*ans[i], sep='')
