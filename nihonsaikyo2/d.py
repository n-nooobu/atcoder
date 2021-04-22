import io
import sys

# input here
_INPUT = """\
45108 2571593

"""
sys.stdin = io.StringIO(_INPUT)



N, P = map(int, input().split())
mod = 10 ** 9 + 7

def pow(s, x, n):
    ans = s
    while n:
        if n % 2:
            ans = (ans * x) % mod
        x = x ** 2 % mod
        n >>= 1
    return ans

ans = pow(P - 1, P - 2, N - 1)
print(ans)
