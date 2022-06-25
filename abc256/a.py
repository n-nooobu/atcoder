import io
import sys

# input here
_INPUT = """\
30

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())

print(pow(2, N))
