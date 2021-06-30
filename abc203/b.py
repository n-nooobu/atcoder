import io
import sys

# input here
_INPUT = """\
3 3

"""
sys.stdin = io.StringIO(_INPUT)



N, K = map(int, input().split())

ans = 0
for i in range(1, N + 1):
    for j in range(1, K + 1):
        ans += int(str(i) + '0' + str(j))

print(ans)
