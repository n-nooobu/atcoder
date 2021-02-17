import io
import sys

# input here
_INPUT = """\

"""
sys.stdin = io.StringIO(_INPUT)



H, W = map(int, input().split())
S = [input() for _ in range(H)]


