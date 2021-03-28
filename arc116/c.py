import io
import sys

# input here
_INPUT = """\

"""
sys.stdin = io.StringIO(_INPUT)



N, M = map(int, input().split())

from collections import Counter

N, M = map(int, input().split())
mod = 998244353

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

class Combination:
    def __init__(self, size):
        self.size = size + 2
        self.fact = [1, 1] + [0] * size
        self.factInv = [1, 1] + [0] * size
        self.inv = [0, 1] + [0] * size
        for i in range(2, self.size):
            self.fact[i] = self.fact[i - 1] * i % mod
            self.inv[i] = -self.inv[mod % i] * (mod // i) % mod
            self.factInv[i] = self.factInv[i - 1] * self.inv[i] % mod

    def npr(self, n, r):
        if n < r or n < 0 or r < 0:
            return 0
        return self.fact[n] * self.factInv[n - r] % mod

    def ncr(self, n, r):
        if n < r or n < 0 or r < 0:
            return 0
        return self.fact[n] * (self.factInv[r] * self.factInv[n - r] % mod) % mod

    def nhr(self, n, r):  # 重複組合せ: x_1 + ... + x_n = r
        return self.ncr(n + r - 1, n - 1)

spf = get_spf(M)
comb = Combination(10 ** 6)
ans = 0
for i in range(1, M + 1):
    factors = []
    while i > 1:
        factors.append(spf[i])
        i //= spf[i]
    c = Counter(factors)
    tmp = 1
    for j in c.values():
        tmp = (tmp * comb.nhr(N, j)) % mod
    ans = (ans + tmp) % mod

print(ans % mod)
