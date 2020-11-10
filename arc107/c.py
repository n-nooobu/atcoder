import io
import sys

# input here
_INPUT = """\
3 13
3 2 7
4 8 9
1 6 5

"""
sys.stdin = io.StringIO(_INPUT)



import itertools

N, K = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(N)]

h = 0
w = 0
for i in itertools.product(range(N), repeat=2):
    if i[0] >= i[1]:
        continue
    for j in range(N):
        if a[i[0]][j] + a[i[1]][j] > K:
            h += 1
            break
for i in itertools.product(range(N), repeat=2):
    if i[0] >= i[1]:
        continue
    for j in range(N):
        if a[j][i[0]] + a[j][i[1]] > K:
            w += 1
            break

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

patern_h = N * (N - 1) // 2 - h
comb_h = Combination(patern_h)
t_h = 0
for i in range(patern_h + 1):
    t_h += comb_h.ncr(patern_h, i)
    t_h %= mod
patern_w = N * (N - 1) // 2 - w
comb_w = Combination(patern_w)
t_w = 0
for i in range(patern_w + 1):
    t_w += comb_w.ncr(patern_w, i)
    t_w %= mod

print(t_h * t_w % mod)
