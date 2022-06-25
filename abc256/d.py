import io
import sys

# input here
_INPUT = """\
2
1 10
11 15
"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
LR = sorted([list(map(int, input().split())) for _ in range(N)])

ans = []
for l, r in LR:
    if len(ans) == 0:
        ans.append([l, r])
    else:
        if r <= ans[-1][1]:
            continue
        else:
            if l > ans[-1][1]:
                ans.append([l, r])
            else:
                p = ans.pop()
                ans.append([p[0], r])

for l, r in ans:
    print(l, r)
