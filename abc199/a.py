import io
import sys

# input here
_INPUT = """\
2 2 4


"""
sys.stdin = io.StringIO(_INPUT)



A, B, C = map(int, input().split())

if A ** 2 + B ** 2 < C ** 2:
    print('Yes')
else:
    print('No')
