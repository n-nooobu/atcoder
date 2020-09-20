import io
import sys

# input here
_INPUT = """\
3 5 -4 -2
"""
sys.stdin = io.StringIO(_INPUT)



a, b, c, d = map(int, input().split())

ans = [0] * 4
ans[0] = a * c
ans[1] = a * d
ans[2] = b * c
ans[3] = b * d

print(max(ans))
