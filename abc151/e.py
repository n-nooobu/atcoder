import io
import sys

# input here
_INPUT = """\
10 6
1000000000 1000000000 1000000000 1000000000 1000000000 0 0 0 0 0

"""
sys.stdin = io.StringIO(_INPUT)



N, K = map(int, input().split())
A = sorted(list(map(int, input().split())))
mod = 10 ** 9 + 7

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

if K == 1:
    print(0)
else:
    comb = Combination(N)
    l = []
    for i in range(K - 2, N - 1):
        l.append(comb.ncr(i, K - 2))
    for i in range(1, N - K + 1):
        l[i] += l[i - 1]

    ans = 0
    l = l[::-1]
    Arev = A[::-1]
    for i in range(N - K + 1):
        ans += l[i] * Arev[i]
        ans %= mod
    for i in range(N - K + 1):
        ans -= l[i] * A[i]
        ans %= mod

    print(ans)
