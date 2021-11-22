import io
import sys

# input here
_INPUT = """\
3.456

"""
sys.stdin = io.StringIO(_INPUT)



X = float(input()) * 1000

if X % 1000 // 100 <= 4:
    print(int(X // 1000))
else:
    print(int(X // 1000 + 1))
