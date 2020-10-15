import io
import sys

# input here
_INPUT = """\
1010101 10


"""
sys.stdin = io.StringIO(_INPUT)



N, K = map(int, input().split())

ans = 0
Kt = 1
while N // Kt:
    ans += 1
    Kt *= K

print(ans)
