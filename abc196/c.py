import io
import sys

# input here
_INPUT = """\
15
"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())

ans = 0
for i in range(1, 10 ** (len(str(N)) // 2)):
    if i + i * 10 ** len(str(i)) <= N:
        ans += 1

print(ans)
