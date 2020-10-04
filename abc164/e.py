import io
import sys

# input here
_INPUT = """\
14282668646
"""
sys.stdin = io.StringIO(_INPUT)



N, M, S = map(int, input().split())
UVAB = [list(map(int, input().split())) for _ in range(M)]
CD = [list(map(int, input().split())) for _ in range(N)]

dp = [[10 ** 11] * (50 * 50) for _ in range(N)]

