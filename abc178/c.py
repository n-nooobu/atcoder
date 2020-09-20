import io
import sys

# input here
_INPUT = """\
869121
"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())

ans = 10 ** N - (9 ** N + 9 ** N - 8 ** N)
ans = ans % (10 ** 9 + 7)

print(ans)
