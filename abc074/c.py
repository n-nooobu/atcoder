import io
import sys

# input here
_INPUT = """\
17 19 22 26 55 2802

"""
sys.stdin = io.StringIO(_INPUT)



A, B, C, D, E, F = map(int, input().split())

ans = [0, 100 * A, 0]
for a in range(1, F + 1):
    for b in range(F - a + 1):
        if 100 * b > E * a:
            continue
        noudo = b / (a + b)
        if noudo > ans[0]:
            for i in range(a // (100 * A) + 1):
                if (a - i * 100 * A) % (100 * B) == 0:
                    for j in range(b // C + 1):
                        if (b - j * C) % D == 0:
                            ans = [noudo, a + b, b]

print(ans[1], ans[2])
