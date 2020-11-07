import io
import sys

# input here
_INPUT = """\
5 1
100 200 300 400 500


"""
sys.stdin = io.StringIO(_INPUT)



N, K = map(int, input().split())
h = list(map(int, input().split()))

ans = 0
for i in range(N):
    if h[i] >= K:
        ans += 1

print(ans)
