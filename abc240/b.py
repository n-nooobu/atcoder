import io
import sys

# input here
_INPUT = """\
11
3 1 4 1 5 9 2 6 5 3 5

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
a = list(map(int, input().split()))

print(len(set(a)))
