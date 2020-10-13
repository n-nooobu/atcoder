import io
import sys

# input here
_INPUT = """\
3
3 1 2
4 2 2
331895368 154715807 13941326

"""
sys.stdin = io.StringIO(_INPUT)



T = int(input())
N = []
A = []
B = []
for i in range(T):
    t = list(map(int, input().split()))
    N.append(t[0])
    A.append(t[1])
    B.append(t[2])

mod = 10 ** 9 + 7

for i in range(T):
    ans = 0
    n = N[i]
    a = A[i]
    b = B[i]
    if n < a + b:
        print(0)
        continue
    ans += (n - a + 1) ** 2 * (n - b + 1) ** 2
    if n - (b - 1) * 2 - a + 1 > 0:
        ans -= (n - (b - 1) * 2 - a + 1) ** 2 * (a + b - 1) ** 2
    ans -= 4 * (n - (b - 1) * 2 - a + 1) * ((b - 1) * (a + b - 1) ** 2 - (a + b - 1) * b * (b - 1) // 2)
    ans -= 4 * (b - 1) ** 2 * (a + b - 1) ** 2 - (b - 1) ** 2 * b * (a * b - 1) // 2 + (b - 1) * (2 - 2 * a - b) * (b - 1) * b //4
    print(ans % mod)
