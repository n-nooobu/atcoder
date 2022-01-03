import io
import sys

# input here
_INPUT = """\
3141

"""
sys.stdin = io.StringIO(_INPUT)



D = int(input())

print(D / 100)
