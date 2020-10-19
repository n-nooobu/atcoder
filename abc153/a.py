import io
import sys

# input here
_INPUT = """\
1 10000

"""
sys.stdin = io.StringIO(_INPUT)



H, A = map(int, input().split())

ans = 0
while H > 0:
    H -= A
    ans += 1

print(ans)
