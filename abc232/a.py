import io
import sys

# input here
_INPUT = """\
3x7

"""
sys.stdin = io.StringIO(_INPUT)



S = input()

print(int(S[0]) * int(S[-1]))
