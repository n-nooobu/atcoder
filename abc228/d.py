import io
import sys

# input here
_INPUT = """\
4
1 1048577
1 1
2 2097153
2 3

"""
sys.stdin = io.StringIO(_INPUT)



Q = int(input())
tx = [list(map(int, input().split())) for _ in range(Q)]

N = pow(2, 20)
A = [-1] * N


