import io
import sys

# input here
_INPUT = """\
6174 100000

"""
sys.stdin = io.StringIO(_INPUT)



N, K = map(int, input().split())

def func(n):
    nums = []
    for i in range(len(str(n))):
        nums.append(n % 10)
        n = n // 10
    nums1 = sorted(nums, reverse=True)
    nums2 = sorted(nums)
    g1 = 0
    g2 = 0
    for i in range(len(nums1)):
        g1 = g1 * 10 + nums1[i]
        g2 = g2 * 10 + nums2[i]
    return g1 - g2

ans = N
for i in range(K):
    ans = func(ans)

print(ans)
