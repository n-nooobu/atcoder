import io
import sys

# input here
_INPUT = """\
1000 1 1

"""
sys.stdin = io.StringIO(_INPUT)



X, Y, Z = map(int, input().split())

ans = 0
for i in range(1000500):
    if Y / X > i / Z:
        ans = max(ans, i)

print(ans)
