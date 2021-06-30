import io
import sys

# input here
_INPUT = """\
3 2
5 5
2 1
2 2

"""
sys.stdin = io.StringIO(_INPUT)



N, K = map(int, input().split())
AB = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: x[0])

now = 0
for i in range(N):
    if AB[i][0] > now + K:
        print(now + K)
        exit()
    else:
        K = K - (AB[i][0] - now) + AB[i][1]
        now = AB[i][0]

print(now + K)
