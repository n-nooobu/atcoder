import io
import sys

# input here
_INPUT = """\
99999 99998


"""
sys.stdin = io.StringIO(_INPUT)



A, B = map(int, input().split())

print((A - B) / A * 100)
