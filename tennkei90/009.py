import io
import sys

# input here
_INPUT = """\
ozRnonnoe

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]


