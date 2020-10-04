import io
import sys

# input here
_INPUT = """\
10 3
1
5
4
3
8
6
9
7
2
4
"""
sys.stdin = io.StringIO(_INPUT)



N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]

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

n = 3 * 10 ** 5
st = SegmentTree(n + 1, segfunc=max, ele=0)
for i in range(N):
    c = st.query(max(0, A[i] - K), min(n + 1, A[i] + K + 1))
    st.update(A[i], c + 1)

print(st.seg[0])
