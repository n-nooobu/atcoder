import io
import sys

# input here
_INPUT = """\
5 6 4


"""
sys.stdin = io.StringIO(_INPUT)



a, b, c = map(int, input().split())

print(21 - a - b - c)
