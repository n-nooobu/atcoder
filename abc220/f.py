import io
import sys

# input here
_INPUT = """\

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
uv = [list(map(int, input().split())) for _ in range(N)]


