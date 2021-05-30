import io
import sys

# input here
_INPUT = """\
998984374864432412

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())

ans = 10 ** 18
two = 1
for i in range(60):
    ans = min(ans, N // two + i + N % two)

    two *= 2

print(ans)
