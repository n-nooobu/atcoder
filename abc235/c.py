import io
import sys

# input here
_INPUT = """\
6 8
1 1 2 3 1 2
1 1
1 2
1 3
1 4
2 1
2 2
2 3
4 1

"""
sys.stdin = io.StringIO(_INPUT)



from collections import defaultdict

N, Q = map(int, input().split())
a = list(map(int, input().split()))

dic = defaultdict(list)
for i in range(N):
    dic[a[i]].append(i + 1)

for q in range(Q):
    x, k = map(int, input().split())

    if len(dic[x]) >= k:
        print(dic[x][k - 1])
    else:
        print(-1)
