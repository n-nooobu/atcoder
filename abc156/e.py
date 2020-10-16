import io
import sys

# input here
_INPUT = """\
15 6

"""
sys.stdin = io.StringIO(_INPUT)



n, k = map(int, input().split())

mod = 10 ** 9 + 7
def combination(n, r):
    bunsi = 1
    for i in range(r):
        bunsi = bunsi * (n - i) % mod
    bunbo = 1
    for i in range(r):
        bunbo = bunbo * (i + 1) % mod
    comb = bunsi * pow(bunbo, mod - 2, mod) % mod
    return comb

if n - k <= 1:
    ans = combination(2 * n - 1, n - 1)
    print(ans)
else:
    bunsi0 = [1] * (n + 1)
    for i in range(1, n + 1):
        bunsi0[i] = bunsi0[i - 1] * (n - i + 1) % mod
    bunbo = [1] * (n + 1)
    for i in range(1, n + 1):
        bunbo[i] = bunbo[i - 1] * i % mod
    comb0 = [0] * (n + 1)
    for i in range(n + 1):
        comb0[i] = bunsi0[i] * pow(bunbo[i], mod - 2, mod) % mod

    bunsi1 = [1] * n
    for i in range(1, n):
        bunsi1[i] = bunsi1[i - 1] * (n - i) % mod
    comb1 = [0] * n
    for i in range(n):
        comb1[i] = bunsi1[i] * pow(bunbo[i], mod - 2, mod) % mod

    ans = 0
    for i in range(k + 1):
        ans = (ans + comb0[i] * comb1[i]) % mod

    print(ans)
