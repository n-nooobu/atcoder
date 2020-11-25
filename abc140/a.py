import io
import sys

# input here
_INPUT = """\
2


"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())

print(N ** 3)
