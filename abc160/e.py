import io
import sys

# input here
_INPUT = """\
2 2 4 4 4
11 12 13 14
21 22 23 24
1 2 3 4

"""
sys.stdin = io.StringIO(_INPUT)



X, Y, A, B, C = map(int, input().split())
p = sorted(list(map(int, input().split())))[-X:]
q = sorted(list(map(int, input().split())))[-Y:]
r = sorted(list(map(int, input().split())))

apple = sorted(p + q + r)
ans = sum(apple[-X-Y:])

print(ans)
