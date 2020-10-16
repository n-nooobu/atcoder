import io
import sys

# input here
_INPUT = """\

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())

A = list(map(int, input().split()))

H, W, M = map(int, input().split())

c = [input() for _ in range(H)]
# ['s####', '....#', '#####', '#...g']
# 文字を変えられない
c = [list(input()) for _ in range(H)]
# [['s', '#', '#', '#', '#'], ['.', '.', '.', '.', '#'], ['#', '#', '#', '#', '#'], ['#', '.', '.', '.', 'g']]
# 文字を変えられる

rcv = [list(map(int, input().split())) for _ in range(K)]
# [[1, 1, 3], [2, 1, 4], [1, 2, 5]]



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


def combination(n, r):
    bunsi = 1
    for i in range(r):
        bunsi = bunsi * (n - i) % mod
    bunbo = 1
    for i in range(r):
        bunbo = bunbo * (i + 1) % mod
    comb = bunsi * pow(bunbo, mod - 2, mod) % mod
    return comb


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):  # 要素xが属するグループの根を返す
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):  # 要素xが属するグループと要素yが属するグループとを併合する
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def same(self, x, y):  # 要素x, yが同じグループに属するかどうかを返す
        return self.find(x) == self.find(y)

    def size(self, x):  # 要素xが属するグループのサイズ（要素数）を返す
        return -self.parents[self.find(x)]

    def members(self, x):  # 要素xが属するグループに属する要素をリストで返す
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):  # すべての根の要素をリストで返す
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):  # グループの数を返す
        return len(self.roots())

    def all_group_members(self):  # {ルート要素: [そのグループに含まれる要素のリスト], ...}の辞書を返す
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):  # ルート要素: [そのグループに含まれる要素のリスト]を文字列で返す
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())



class SegmentTree:
    def __init__(self, n, segfunc=min, ele=10**10):
        self.n, self.segfunc, self.ide_ele = n, segfunc, ele
        self.num = 2 ** (n - 1).bit_length()
        self.seg = [self.ide_ele] * 2 * self.num

    def init(self, init_val):
        for i in range(self.n):
            self.seg[i + self.num - 1] = init_val[i]
        for i in range(self.num - 2, -1, -1):
            self.seg[i] = self.segfunc(self.seg[2 * i + 1], self.seg[2 * i + 2])

    def update(self, k, x):
        k += self.num - 1
        self.seg[k] = x
        while k:
            k = (k - 1) // 2
            self.seg[k] = self.segfunc(self.seg[k * 2 + 1], self.seg[k * 2 + 2])

    def query(self, p, q):
        if q <= p:
            return self.ide_ele
        p += self.num - 1
        q += self.num - 2
        res = self.ide_ele
        while q - p > 1:
            if p & 1 == 0:
                res = self.segfunc(res, self.seg[p])
            if q & 1 == 1:
                res = self.segfunc(res, self.seg[q])
                q -= 1
            p = p // 2
            q = (q - 1) // 2
        if p == q:
            res = self.segfunc(res, self.seg[p])
        else:
            res = self.segfunc(self.segfunc(res, self.seg[p]), self.seg[q])
        return res

    def get_val(self, k):
        k += self.num - 1
        return self.seg[k]
