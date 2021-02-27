import io
import sys

# input here
_INPUT = """\
100000
3226#
3597#




"""
sys.stdin = io.StringIO(_INPUT)



from collections import Counter

K = int(input())
S = input()
T = input()

t = Counter(S[:-1] + '123456789')
a = Counter(T[:-1] + '123456789')
t_score = 0
a_score = 0
for n, c in t.items():
    t_score += int(n) * 10 ** (c - 1)
for n, c in a.items():
    a_score += int(n) * 10 ** (c - 1)

ans = 0
for i in range(1, 10):
    taka = t_score - i * 10 ** (t[str(i)] - 1) + i * 10 ** t[str(i)]
    for j in range(1, 10):
        aoki = a_score - j * 10 ** (a[str(j)] - 1) + j * 10 ** a[str(j)]
        if taka > aoki:
            if i == j:
                ans += (K - (t[str(i)] - 1) - (a[str(i)] - 1)) / (9 * K - 8) * (K - (t[str(j)] - 1) - (a[str(j)] - 1) - 1) / (9 * K - 9)
            else:
                ans += (K - (t[str(i)] - 1) - (a[str(i)] - 1)) / (9 * K - 8) * (K - (t[str(j)] - 1) - (a[str(j)] - 1)) / (9 * K - 9)
print(ans)
