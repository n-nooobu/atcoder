import io
import sys

# input here
_INPUT = """\
10 13 15
3
1
4
1
5
9
2
6
5
3
5
8
9
7
9


"""
sys.stdin = io.StringIO(_INPUT)



N, K, Q = map(int, input().split())

correct = [0] * (N + 1)
for i in range(Q):
    a = int(input())
    correct[a] += 1

for i in range(1, N + 1):
    if K - (Q - correct[i]) < 1:
        print('No')
    else:
        print('Yes')
