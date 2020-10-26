import io
import sys

# input here
_INPUT = """\
3
28 27 24

"""
sys.stdin = io.StringIO(_INPUT)



import sys

N = int(input())
A = list(map(int, input().split()))

for i in range(N):
    if A[i] % 2 == 0:
        if A[i] % 3 == 0 or A[i] % 5 == 0:
            continue
        else:
            print('DENIED')
            sys.exit()

print('APPROVED')
