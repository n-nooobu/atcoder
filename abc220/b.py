import io
import sys

# input here
_INPUT = """\
7
123 456

"""
sys.stdin = io.StringIO(_INPUT)



K = int(input())
A, B = map(int, input().split())

print(int(str(A), K) * int(str(B), K))
