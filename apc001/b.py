import io
import sys

# input here
_INPUT = """\
5
2 7 1 8 2
3 1 4 1 5

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

k = sum(b) - sum(a)
if k < 0:
    print('No')
else:
    cnt = 0
    for i in range(N):
        if a[i] < b[i]:
            cnt += (b[i] - a[i]) // 2 + (b[i] - a[i]) % 2
    if cnt <= k:
        print('Yes')
    else:
        print('No')
