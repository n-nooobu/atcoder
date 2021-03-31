import io
import sys

# input here
_INPUT = """\
27182818284590


"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())

ans = 0
for i in range(6):
    if 10 ** (i * 3) <= N < 10 ** ((i + 1) * 3):
        ans += (N - 10 ** (i * 3) + 1) * i
        break
    else:
        ans += (10 ** ((i + 1) * 3) - 10 ** (i * 3)) * i

print(ans)
