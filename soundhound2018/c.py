import io
import sys

# input here
_INPUT = """\
1000000000 180707 0


"""
sys.stdin = io.StringIO(_INPUT)



n, m, d = map(int, input().split())

if d == 0:
    print(1 / n * (m - 1))
else:
    print(2 * (n - d) / n ** 2 * (m - 1))
