import io
import sys

# input here
_INPUT = """\
10
1 2 3


"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
coin = list(map(int, input().split()))

ans = 10 ** 5
for i in range(10 ** 4, -1, -1):
    for j in range(10 ** 4 - i, -1, -1):
        rest = N - coin[0] * i - coin[1] * j
        k = i + j + rest // coin[2]
        if rest >= 0 and rest % coin[2] == 0 and k < 10 ** 4:
            ans = min(ans, k)

print(ans)
