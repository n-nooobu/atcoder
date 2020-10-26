import io
import sys

# input here
_INPUT = """\
1
1

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
a = list(map(int, input().split()))

need = 1
for i in range(N):
    if a[i] == need:
        need += 1

if need == 1:
    print(-1)
else:
    print(N - (need - 1))
