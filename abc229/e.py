import io
import sys

# input here
_INPUT = """\
8 7
7 8
3 4
5 6
5 7
5 8
6 7
6 8

"""
sys.stdin = io.StringIO(_INPUT)



from collections import defaultdict
import sys
sys.setrecursionlimit(int(1e7))

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]

G = defaultdict(set)
for i in range(M):
    A = AB[i][0] - 1
    B = AB[i][1] - 1
    G[A].add(B)
    G[B].add(A)

class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
        self.r = n

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
        self.r -= 1

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
        return self.r  #len(self.roots())

    def all_group_members(self):  # {ルート要素: [そのグループに含まれる要素のリスト], ...}の辞書を返す
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):  # ルート要素: [そのグループに含まれる要素のリスト]を文字列で返す
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

ans = [0]
uf = UnionFind(N)
for i in reversed(range(1, N)):
    for v in G[i]:
        if v > i:
            uf.union(i, v)
    ans.append(uf.r - i)

for i in reversed(range(len(ans))):
    print(ans[i])
