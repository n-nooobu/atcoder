import io
import sys

# input here
_INPUT = """\
19 99

"""
sys.stdin = io.StringIO(_INPUT)



import sys

A, B = map(int, input().split())

for i in range(2 * 10 ** 3):
    if (A / 0.08 <= i < (A + 1) / 0.08) and (B / 0.1 <= i < (B + 1) / 0.1):
        print(i)
        sys.exit()

print(-1)
