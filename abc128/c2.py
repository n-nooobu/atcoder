import io
import sys

# input here
_INPUT = """\
5 2
3 1 2 5
2 2 3
1 0

"""
sys.stdin = io.StringIO(_INPUT)



N, M = map(int, input().split())
s = [list(map(int, input().split()))[1:] for _ in range(M)]
p = list(map(int, input().split()))

ans = 0
for i in range(1 << N):
    bit = [i >> j for j in range(N)]
    for k in range(M):
        if p[k] != sum([bit[l - 1] for l in s[k]]) % 2:
            break
    else:
        ans += 1

print(ans)
