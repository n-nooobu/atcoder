import io
import sys

# input here
_INPUT = """\
123456789 9876543210

"""
sys.stdin = io.StringIO(_INPUT)



import sys

A, B = input().split()
A = A.zfill(19)
B = B.zfill(19)

for i in range(len(A)):
    if int(A[i]) + int(B[i]) >= 10:
        print('Hard')
        sys.exit()

print('Easy')
