import io
import sys

# input here
_INPUT = """\
99999999
99999999
"""
sys.stdin = io.StringIO(_INPUT)



A = int(input())
B = int(input())

ans = str(A)
if B % 2:
    ans += str(B // 2) + '5'
else:
    ans += str(B // 2) + '0'

print(ans)
