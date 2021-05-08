import io
import sys

# input here
_INPUT = """\
3 3
10
1 2 2
1 1 1
2 1 1 2 2
1 3 2
2 1 1 2 2
2 2 2 3 2
1 2 3
1 2 1
2 1 1 2 2
2 1 1 3 3


"""
sys.stdin = io.StringIO(_INPUT)



H, W = map(int, input().split())
Q = int(input())

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

color = [[0] * W for _ in range(H)]
uf = UnionFind(H * W + 1)
for i in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        r, c = q[1] - 1, q[2] - 1
        color[r][c] = 1
        for rc, cc in [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]:
            if 0 <= rc < H and 0 <= cc < W and color[rc][cc]:
                uf.union(r * W + c, rc * W + cc)
    else:
        ra, ca, rb, cb = q[1] - 1, q[2] - 1, q[3] - 1, q[4] - 1
        if color[ra][ca] and color[rb][cb] and uf.same(ra * W + ca, rb * W + cb):
            print('Yes')
        else:
            print('No')
