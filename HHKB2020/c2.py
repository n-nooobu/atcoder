import io
import sys

# input here
_INPUT = """\
4
1 1 0 2

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
p = list(map(int, input().split()))
ans = 0
appeared = [False] * (N + 1)
for i in range(N):
    if p[i] <= N:
        appeared[p[i]] = True
    while appeared[ans]:
        ans += 1
    print(ans)
