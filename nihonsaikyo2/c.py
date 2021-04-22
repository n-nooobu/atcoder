import io
import sys

# input here
_INPUT = """\
199999 200000

"""
sys.stdin = io.StringIO(_INPUT)



A, B = map(int, input().split())

ans = 1
for i in range(1, B):
    if (B // i - 1) * i >= A:
        ans = i

print(ans)
