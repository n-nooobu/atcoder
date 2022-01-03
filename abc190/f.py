import io
import sys

# input here
_INPUT = """\
10
0 3 1 5 4 2 9 6 8 7
"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
a = list(map(int, input().split()))

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
    ans += i - bit.sum(a[i] + 1)
    bit.add(a[i] + 1, 1)

print(ans)
for i in range(N - 1):
    ans += N - 1 - 2 * a[i]
    print(ans)
