import io
import sys

# input here
_INPUT = """\
3
2
998244353
1000000000000000000

"""
sys.stdin = io.StringIO(_INPUT)



T = int(input())

for i in range(T):
    num = 0
    N = int(input())
    while N % 2 == 0:
        N //= 2
        num += 1
    if num == 0:
        print('Odd')
    elif num == 1:
        print('Same')
    else:
        print('Even')
