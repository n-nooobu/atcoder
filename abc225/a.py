import io
import sys

# input here
_INPUT = """\
xyz

"""
sys.stdin = io.StringIO(_INPUT)



S = input()

if S[0] != S[1] and S[2] != S[1] and S[2] != S[0]:
    print(6)
elif S[0] == S[1] and S[2] == S[1]:
    print(1)
else:
    print(3)
