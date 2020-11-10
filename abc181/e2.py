import io
import sys

# input here
_INPUT = """\
5 3
1 2 3 4 7
1 1 1

"""
sys.stdin = io.StringIO(_INPUT)



from bisect import bisect_left

N, M = map(int, input().split())
H = sorted(list(map(int, input().split())))
W = sorted(list(map(int, input().split())))

first_cost = 0
for i in range(1, N, 2):
    first_cost += H[i + 1] - H[i]

pair_costs = [0] * (N // 2 + 1)
pair_costs[0] = first_cost
for i in range(1, N // 2 + 1):
    pair_costs[i] = pair_costs[i - 1] - (H[i * 2] - H[i * 2 - 1]) + (H[(i - 1) * 2 + 1] - H[(i - 1) * 2])

ans = 10 ** 18
now_id = 0
for i in range(len(pair_costs)):
    if len(W) > 1:
        if 0 <= bisect_left(W, H[i * 2]) - 1 < len(W):
            ans = min(ans, pair_costs[i] + abs(W[bisect_left(W, H[i * 2]) - 1] - H[i * 2]))
        if 0 <= bisect_left(W, H[i * 2]) < len(W):
            ans = min(ans, pair_costs[i] + abs(W[bisect_left(W, H[i * 2])] - H[i * 2]))
    else:
        ans = min(ans, pair_costs[i] + abs(W[0] - H[i * 2]))

print(ans)
