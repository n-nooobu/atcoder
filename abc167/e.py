import io
import sys

# input here
_INPUT = """\
60522 114575 7559
"""
sys.stdin = io.StringIO(_INPUT)



N, M, K = map(int, input().split())

mod = 998244353
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

ans = 0
m = M
comb = Combination(N)
for k in reversed(range(N)):
    now = m
    now *= comb.ncr(N - 1, k)
    now %= mod
    if k <= K:
        ans += now
        ans %= mod
    m *= M - 1
    m %= mod

print(ans)
