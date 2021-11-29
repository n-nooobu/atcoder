import io
import sys

# input here
_INPUT = """\
10 3141
314944731 649
140276783 228
578012421 809
878510647 519
925326537 943
337666726 611
879137070 306
87808915 39
756059990 244
228622672 291

"""
sys.stdin = io.StringIO(_INPUT)



N, W = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
AB = sorted(AB, reverse=True)

ans = 0
idx = 0
while idx < N:
    if AB[idx][1] <= W:
        W -= AB[idx][1]
        ans += AB[idx][0] * AB[idx][1]
        idx += 1
    else:
        ans += AB[idx][0] * W
        break

print(ans)
