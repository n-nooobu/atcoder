import io
import sys

# input here
_INPUT = """\
101

"""
sys.stdin = io.StringIO(_INPUT)



N = input()

print(N[-2:])
