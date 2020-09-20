import io
import sys

# input here
_INPUT = """\
apple
"""
sys.stdin = io.StringIO(_INPUT)



S = input()

if S[-1] == 's':
    print(S + 'es')
else:
    print(S + 's')
