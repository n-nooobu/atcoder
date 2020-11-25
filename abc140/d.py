import io
import sys

# input here
_INPUT = """\

"""
sys.stdin = io.StringIO(_INPUT)



N, K = map(int, input().split())
S = input()

LRRLRLRRLRLLR 13 9
LRRRLLRRLRLLR
LRRRLLLLRLRRR
LRRRRRRRLRRRR

LRRLRLRRLRLLR
LRRLRLLLLRLLR
LRRLRRRRRRLLR
LRRLLLLLLLLLR