import io
import sys

# input here
_INPUT = """\
2 -2
"""
sys.stdin = io.StringIO(_INPUT)



A, B = map(int, input().split())

print((A + B) // 2, (A - B) // 2)
