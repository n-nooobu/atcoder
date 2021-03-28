import io
import sys

# input here
_INPUT = """\
abc

"""
sys.stdin = io.StringIO(_INPUT)



S = input()

print(S[1:] + S[0])
