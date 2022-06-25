import io
import sys

# input here
_INPUT = """\
7 5
1 2 3 4 5 5 10

"""
sys.stdin = io.StringIO(_INPUT)



import sys

N, K = map(int, input().split())
a = list(map(int, input().split()))

for i in range(K):
    a[i::K] = sorted(a[i::K])

for i in range(N - 1):
    if a[i] > a[i + 1]:
        print('No')
        sys.exit()

print('Yes')
