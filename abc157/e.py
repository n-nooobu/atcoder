import io
import sys

# input here
_INPUT = """\
7
abcdbbd
6
2 3 6
1 5 z
2 1 1
1 4 a
1 7 d
2 1 7


"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
S = input()
Q = int(input())
Query = [list(input().split()) for _ in range(Q)]

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

def op(a, b):
    return a | b

st = SegmentTree(N, segfunc=op, ele=0)
character = []
for i in range(26):
    character.append([chr(i + ord('a')), 1 << i])
init_val = [0] * N
for i in range(N):
    for j in range(26):
        if character[j][0] == S[i]:
            init_val[i] = character[j][1]
st.init(init_val)

for i in range(Q):
    if Query[i][0] == '1':
        st.update(int(Query[i][1]) - 1, character[ord(Query[i][2]) - ord('a')][1])
    else:
        res = st.query(int(Query[i][1]) - 1, int(Query[i][2]))
        print(bin(res).count('1'))
