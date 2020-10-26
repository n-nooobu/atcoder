import io
import sys

# input here
_INPUT = """\
4 100 60
0 0 0

"""
sys.stdin = io.StringIO(_INPUT)



N, K, M = map(int, input().split())
A = list(map(int, input().split()))

ans = N * M - sum(A)
if 0 <= ans <= K:
    print(ans)
elif ans < 0:
    print(0)
else:
    print(-1)
