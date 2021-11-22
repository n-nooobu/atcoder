import io
import sys

# input here
_INPUT = """\
1
83322293 97603739 49636406

"""
sys.stdin = io.StringIO(_INPUT)



T = int(input())
for t in range(T):
    R, G, B = map(int, input().split())
    ans = -1
    for a, b, c in [[R, G, B], [G, R, B], [B, R, G]]:
        M = max(b, c)
        m = min(b, c)
        if (M - m) % 3 == 0:
            tmp = (M - m) // 3
            if ans != -1:
                ans = min(ans, m + 3 * tmp)
            else:
                ans = m + 3 * tmp
    print(ans)
