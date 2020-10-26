import io
import sys

# input here
_INPUT = """\

"""
sys.stdin = io.StringIO(_INPUT)



N = input()
K = int(input())

def combination(n, r):
    comb = 1
    for i in range(r):
        comb *= n - i
    for i in range(r):
        comb /= i + 1

ans = 0
for i in range(K, len(N) + 1):
    if i == len(N):
        ans += (N[0] - 1) * combination(i - 1, K - 1) * 9 ** (K - 1)
    else:
        ans += 9 * combination(i - 1, K - 1) * 9 ** (K - 1)

    for
