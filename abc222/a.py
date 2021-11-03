import io
import sys

# input here
_INPUT = """\
7777

"""
sys.stdin = io.StringIO(_INPUT)



N = input()

print('0' * (4 - len(N)) + N)
