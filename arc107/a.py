import io
import sys

# input here
_INPUT = """\
1000000000 987654321 123456789

"""
sys.stdin = io.StringIO(_INPUT)



A, B, C = map(int, input().split())

ans = A * (A + 1) * B * (B + 1) * C * (C + 1) // 8
print(ans % 998244353)
