import io
import sys

# input here
_INPUT = """\
4 3

"""
sys.stdin = io.StringIO(_INPUT)



a, b = map(int, input().split())

m = min(a, b)
M = max(a, b)
ans = ''
for i in range(M):
    ans += str(m)

print(ans)
