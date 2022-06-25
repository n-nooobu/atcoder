import io
import sys

# input here
_INPUT = """\
254

"""
sys.stdin = io.StringIO(_INPUT)



from collections import Counter

N = int(input())

def get_spf(n):
    spf = [i for i in range(n + 1)]
    p = 2
    while p ** 2 <= n:
        if spf[p] == p:
            for q in range(2 * p, n + 1, p):
                if spf[q] == q:
                    spf[q] = p
        p += 1
    return spf

square = []
for i in range(1, int(N ** 0.5) + 1):
    square.append(i ** 2)

spf = get_spf(N)

ans = 0
for i in range(1, N + 1):
    factors = []
    while i > 1:
        factors.append(spf[i])
        i //= spf[i]

    c = Counter(factors)
    tmp = 1
    for key, value in c.items():
        if value % 2 == 1:
            tmp *= key

    for j in square:
        if j * tmp <= N:
            ans += 1

print(ans)
