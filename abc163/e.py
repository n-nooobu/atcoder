import io
import sys

# input here
_INPUT = """\
6
8 6 9 1 2 1
"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
A = list(map(int, input().split()))

m = []
for i in range(N):
    m.append([max(A), A.index(max(A))])
    A[A.index(max(A))] = 0

ans = 0
l = 0
r = 0
for i in range(N):
    if N % 2 == 0:
        if m[i][1] >= N // 2:
            ans += m[i][0] * (m[i][1] - l)
            l += 1
        else:
            ans += m[i][0] * (N - 1 - r - m[i][1])
            r += 1
    else:
        if m[i][1] > N // 2:
            ans += m[i][0] * (m[i][1] - l)
            l += 1
        elif m[i][1] < N // 2:
            ans += m[i][0] * (N - 1 - r - m[i][1])
            r += 1
        else:
            if l <= r:
                ans += m[i][0] * (m[i][1] - l)
                l += 1
            else:
                ans += m[i][0] * (N - 1 - r - m[i][1])
                r += 1

print(ans)
