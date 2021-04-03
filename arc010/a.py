import io
import sys

# input here
_INPUT = """\
8
-1 10 -1 2 -1 10 -1 0

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
a = list(map(int, input().split()))

INF = 10 ** 5
taka = -INF
for i in range(N):
    aoki = -INF
    for j in range(N):
        if i == j:
            continue
        aoki_tmp = 0
        for k in range(abs(i - j) + 1):
            if k % 2:
                aoki_tmp += a[min(i, j) + k]
        if aoki < aoki_tmp:
            aoki = aoki_tmp
            idx_aoki = j
    taka_tmp = 0
    for j in range(abs(i - idx_aoki) + 1):
        if not j % 2:
            taka_tmp += a[min(i, idx_aoki) + j]
    taka = max(taka, taka_tmp)

print(taka)
