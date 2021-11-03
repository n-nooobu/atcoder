import io
import sys

# input here
_INPUT = """\
3 90
89 89 89

"""
sys.stdin = io.StringIO(_INPUT)



N, P = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for i in range(N):
    if a[i] < P:
        ans += 1

print(ans)
