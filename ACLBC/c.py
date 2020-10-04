import io
import sys

# input here
_INPUT = """\
8 5
1 2
2 3
3 6
4 5
7 8
"""
sys.stdin = io.StringIO(_INPUT)



N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]

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

uf = UnionFind(N)
for i in range(M):
    uf.union(AB[i][0] - 1, AB[i][1] - 1)
print(uf.group_count() - 1)
