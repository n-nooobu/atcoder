import io
import sys

# input here
_INPUT = """\

"""
sys.stdin = io.StringIO(_INPUT)



X = int(input())

ans = 0
ans += X // 500 * 1000
ans += X % 500 // 5 * 5
print(ans)
