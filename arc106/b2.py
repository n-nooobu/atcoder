import io
import sys

# input here
_INPUT = """\
17 9
-905371741 -999219903 969314057 -989982132 -87720225 -175700172 -993990465 929461728 895449935 -999016241 782467448 -906404298 578539175 9684413 -619191091 -952046546 125053320
-440503430 -997661446 -912471383 -995879434 932992245 -928388880 -616761933 929461728 210953513 -994677396 648190629 -530944122 578539175 9684413 595786809 -952046546 125053320
2 10
6 12
9 11
11 5
7 6
3 15
3 1
1 9
10 4


"""
sys.stdin = io.StringIO(_INPUT)



import sys
from collections import deque
from collections import defaultdict

N, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
cd = [list(map(int, input().split())) for _ in range(M)]
G = defaultdict(set)
for i in range(M):
    A = cd[i][0]
    B = cd[i][1]
    G[A].add(B)
    G[B].add(A)

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

uf = UnionFind(N + 1)
for i in range(M):
    uf.union(cd[i][0], cd[i][1])

root = uf.roots()
group = uf.all_group_members()
for i in range(1, len(root)):
    v = group[root[i]]
    e = [0] * (N + 1)
    for j in v:
        e[j] = b[j - 1] - a[j - 1]
    if sum(e) % 2 == 1:
        print('No')
        sys.exit()
    color = [0] * (N + 1)
    color[root[i]] = 1
    que = deque([])
    que.append(root[i])
    while que:
        p = que.popleft()
        for q in list(G[p]):
            if color[q] == 0:
                color[q] = -color[p]
                que.append(q)
    black = 0
    white = 0
    for k, col in enumerate(color):
        if k == 0:
            continue
        if col == 1:
            black += e[k]
        elif col == -1:
            white += e[k]

    if black != white:
        print('No')
        sys.exit()

print('Yes')
