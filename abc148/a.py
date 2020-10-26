import io
import sys

# input here
_INPUT = """\
3
1

"""
sys.stdin = io.StringIO(_INPUT)



A = int(input())
B = int(input())

ans = [1, 2, 3]
ans[A - 1] = 0
ans[B - 1] = 0
print(sum(ans))
