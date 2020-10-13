import io
import sys

# input here
_INPUT = """\
8 0 4

"""
sys.stdin = io.StringIO(_INPUT)



N, A, B = map(int, input().split())

sho = N // (A + B)
yo = N % (A + B)
if yo > A:
    print(sho * A + A)
else:
    print(sho * A + yo)
