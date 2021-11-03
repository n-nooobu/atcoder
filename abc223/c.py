import io
import sys

# input here
_INPUT = """\
3
1 3
2 2
3 1

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

time = 0
for i in range(N):
    time += AB[i][0] / AB[i][1]

time2 = time / 2

ans = 0
for i in range(N):
    if time2 > AB[i][0] / AB[i][1]:
        time2 -= AB[i][0] / AB[i][1]
        ans += AB[i][0]
    else:
        ans += time2 * AB[i][1]
        break

print(ans)
