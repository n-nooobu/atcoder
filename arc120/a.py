import io
import sys

# input here
_INPUT = """\
3
1 2 3


"""
sys.stdin = io.StringIO(_INPUT)



from itertools import accumulate

N = int(input())
A = list(map(int, input().split()))

cuma = list(accumulate(A))
cumb = list(accumulate(cuma))

malist = [0] * N
ma = 0
for i in range(N):
    ma = max(ma, A[i])
    malist[i] = ma

for i in range(N):
    print(cumb[i] + malist[i] * (i + 1))
