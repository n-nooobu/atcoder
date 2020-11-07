import io
import sys

# input here
_INPUT = """\
7
218 786 704 233 645 728 389


"""
sys.stdin = io.StringIO(_INPUT)



import itertools

N = int(input())
L = sorted(list(map(int, input().split())))

ans = 0
for i in itertools.combinations(range(N), 2):
    l = L[i[1] + 1:]
    low = 0
    high = len(l) - 1
    mid = (high + low) // 2
    while high - low > 1:
        if L[i[0]] + L[i[1]] > l[mid]:
            low = mid
        else:
            high = mid
        mid = (high + low) // 2
    if len(l) > 0 and L[i[0]] + L[i[1]] > l[high]:
        ans += high + 1
    elif len(l) > 0 and L[i[0]] + L[i[1]] > l[low]:
        ans += low + 1

print(ans)
