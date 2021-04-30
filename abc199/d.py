import io
import sys

# input here
_INPUT = """\
3 0



"""
sys.stdin = io.StringIO(_INPUT)



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

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
uf = UnionFind(N)
G = [[False] * N for _ in range(N)]
for i in range(M):
    A = AB[i][0] - 1
    B = AB[i][1] - 1
    G[A][B] = G[B][A] = True
    uf.union(A, B)

def dfs(i):
    if i == len(l):
        return 1
    used = [False] * 3
    v = l[i]
    count = 0
    for w in range(N):
        if G[v][w] and color[w] >= 0:
            used[color[w]] = True
    for c in range(3):
        if not used[c]:
            color[v] = c
            count += dfs(i+1)
            color[v] = -1
    return count

dic = uf.all_group_members()

ans = 1
for l in dic.values():
    color = [-1] * N
    color[l[0]] = 0
    ans *= dfs(1) * 3

print(ans)
