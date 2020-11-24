import io
import sys

# input here
_INPUT = """\
1000000000000 1

"""
sys.stdin = io.StringIO(_INPUT)



S, P = map(int, input().split())

for i in range(1, 10 ** 6 + 1):
    if P % i == 0:
        if i + P // i == S:
            print('Yes')
            exit()

print('No')
