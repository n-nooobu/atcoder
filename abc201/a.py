import io
import sys

# input here
_INPUT = """\
5 5 5


"""
sys.stdin = io.StringIO(_INPUT)



A = sorted(list(map(int, input().split())))

if A[2] - A[1] != A[1] - A[0]:
    print('No')
else:
    print('Yes')
