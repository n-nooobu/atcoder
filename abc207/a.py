import io
import sys

# input here
_INPUT = """\
3 4 5

"""
sys.stdin = io.StringIO(_INPUT)



A, B, C = map(int, input().split())

ans = 0
ans = max(A + B, ans)
ans = max(A + C, ans)
ans = max(B + C, ans)

print(ans)
