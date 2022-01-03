import io
import sys

# input here
_INPUT = """\

"""
sys.stdin = io.StringIO(_INPUT)



M = int(input())
uv = [list(map(int, input().split())) for _ in range(M)]
p = list(map(int, input().split()))
