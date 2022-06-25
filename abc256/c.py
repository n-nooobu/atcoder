import io
import sys

# input here
_INPUT = """\
5 13 10 6 13 9

"""
sys.stdin = io.StringIO(_INPUT)



h1, h2, h3, w1, w2, w3 = map(int, input().split())

ans = 0
for a00 in range(1, 30):
    for a01 in range(1, 30):
        a02 = h1 - (a00 + a01)
        if a02 <= 0:
            continue
        for a10 in range(1, 30):
            a20 = w1 - (a00 + a10)
            if a20 <= 0:
                continue
            for a11 in range(1, 30):
                a12 = h2 - (a10 + a11)
                if a12 <= 0:
                    continue
                a21 = w2 - (a01 + a11)
                if a21 <= 0:
                    continue
                a22 = h3 - (a20 + a21)
                if a22 <= 0 or a22 != w3 - (a02 + a12):
                    continue
                ans += 1

print(ans)
