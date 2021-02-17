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
ks = [list(map(int, input().split())) for _ in range(M)]
p = list(map(int, input().split()))

ans = 0
for bit in range(1 << N):
    flag = True
    for m in range(M):
        ons = 0
        for k in range(ks[m][0]):
            if bit & 1 << (ks[m][k + 1] - 1):
                ons += 1
        if ons % 2 != p[m]:
            flag = False
    if flag:
        ans += 1

print(ans)
