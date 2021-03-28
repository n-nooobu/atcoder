import io
import sys

# input here
_INPUT = """\
3 4

"""
sys.stdin = io.StringIO(_INPUT)




N, M = map(int, input().split())

if M % 2:
    print(0)
else:

