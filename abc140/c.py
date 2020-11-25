import io
import sys

# input here
_INPUT = """\
2
3


"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
B = list(map(int, input().split()))

ans = B[0]
for i in range(1, N - 1):
    ans += min(B[i], B[i - 1])
ans += B[-1]

print(ans)
