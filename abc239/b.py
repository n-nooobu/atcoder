import io
import sys

# input here
_INPUT = """\
-24

"""
sys.stdin = io.StringIO(_INPUT)



X = int(input())

print(X // 10)
