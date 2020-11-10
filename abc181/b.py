import io
import sys

# input here
_INPUT = """\
1
1 1000000

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(N):
    ans += (AB[i][0] + AB[i][1]) * (AB[i][1] - AB[i][0] + 1) // 2

print(ans)
