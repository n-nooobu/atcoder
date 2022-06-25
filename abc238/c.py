import io
import sys

# input here
_INPUT = """\
999999999999999999

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
mod = 998244353

ans = 0
for i in range(len(str(N)) - 1):
    ans += (1 + 9 * 10 ** i) * 9 * 10 ** i // 2
    ans %= mod
ans += (N - 10 ** (len(str(N)) - 1) + 1) * (N - 10 ** (len(str(N)) - 1) + 2) // 2
ans %= mod

print(ans)
