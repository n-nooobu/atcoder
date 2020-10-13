import io
import sys

# input here
_INPUT = """\
1 1

"""
sys.stdin = io.StringIO(_INPUT)



N, M = map(int, input().split())

print(N * (N - 1) // 2 + M * (M - 1) // 2)
