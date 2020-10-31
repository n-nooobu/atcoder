import io
import sys

# input here
_INPUT = """\

"""
sys.stdin = io.StringIO(_INPUT)



N, T = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]


