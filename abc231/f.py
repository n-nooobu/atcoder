import io
import sys

# input here
_INPUT = """\
10
3 1 4 1 5 9 2 6 5 3
2 7 1 8 2 8 1 8 2 8

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

def coordinate_compress(a, duplicate=True):
    if duplicate:
        b = sorted(set(a))
        dic = {v: i for i, v in enumerate(b)}
        return list(map(lambda v: dic[v], a))
    else:
        b = sorted(a)
        dic = {v: i for i, v in enumerate(b)}
        c = []
        for v in a:
            c.append(dic[v])
            dic[v] -= 1
        return c

A = coordinate_compress(A, duplicate=True)
B = coordinate_compress(B, duplicate=True)
AB = sorted(list(zip(A, B)), key=lambda x: x[0])

b = sorted([v[1] for v in AB])
dic = {v: i for i, v in enumerate(b)}
c = []
for v in AB:
    c.append(dic[v[1]])
    dic[v[1]] -= 1

class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

bit = Bit(N)
ans = 0
for i in range(N):
    ans += i + 1 - bit.sum(c[i] + 1)
    bit.add(c[i] + 1, 1)

print(ans + N)
