import io
import sys

# input here
_INPUT = """\
2 2
1 2
3 4

"""
sys.stdin = io.StringIO(_INPUT)



R, C = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(2)]

print(A[R - 1][C - 1])
