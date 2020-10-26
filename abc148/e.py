import io
import sys

# input here
_INPUT = """\
1000000000000000000

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())

if N % 2 == 1:
    print(0)
else:
    five = N // 10
    ans = five
    for i in range(25):
        five //= 5
        ans += five
    print(ans)
