import io
import sys

# input here
_INPUT = """\
999999 999999


"""
sys.stdin = io.StringIO(_INPUT)



X, Y = map(int, input().split())

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

flag = False
for i in range(min(X, Y)):
    if (X - 3 * i) * 2 == Y - 3 * i or X - 3 * i == (Y - 3 * i) * 2:
        n = i
        tot = 2 * n + min(X - 3 * i, Y - 3 * i)
        flag = True
        break

if flag:
    comb = Combination(tot)
    print(comb.ncr(tot, n))
else:
    print(0)
