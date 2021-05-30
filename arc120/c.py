import io
import sys

# input here
_INPUT = """\
6
8 5 4 7 4 5
10 5 6 7 4 1


"""
sys.stdin = io.StringIO(_INPUT)



from collections import OrderedDict

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

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

A = [A[i] + i for i in range(N)]
B = [B[i] + i for i in range(N)]

dic = OrderedDict()
for i in range(N - 1, -1, -1):
    if B[i] in dic:
        dic[B[i]].append(i)
    else:
        dic[B[i]] = [i]
idx = [0] * N
for i in range(N):
    if not A[i] in dic or not dic[A[i]]:
        print(-1)
        exit()
    idx[i] = dic[A[i]].pop()

bit = Bit(N)
ans = 0
for i in range(N):
    ans += i - bit.sum(idx[i] + 1)
    bit.add(idx[i] + 1, 1)

print(ans)
