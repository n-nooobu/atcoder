import io
import sys

# input here
_INPUT = """\
7 
"""
sys.stdin = io.StringIO(_INPUT)



A, B, C = map(int, input().split())

def roop(x, y):
    s = x % 10
    nums = [s]
    now = nums[-1] * s % 10
    while now not in nums:
        nums.append(now)
        now = nums[-1] * s % 10
    for i, num in enumerate(nums):
        if nums[i] == now:
            r = len(nums) - i
    return r, nums[y % r - 1], nums

if A % 10 == 1:
    print(1)
elif A % 10 == 5:
    print(5)
elif A % 10 == 6:
    print(6)
elif A % 10 == 4 or A % 10 == 9:
    r, h, nums = roop(B, C)
    r2, h2, nums2 = roop(A, 1)
    if h % 2 == 1:
        print(nums2[0])
    else:
        print(nums2[1])
else:
    r, h, nums = roop(B, C)
    r2, h2, nums2 = roop(A, 1)
    if B == 1:
        print(nums2[0])
    elif 1 < B < 100:
        if C > 10:
            if h % r == 0:
                print(nums2[3])
            else:
                print(nums2[h % r - 1])
        elif pow(B, C) >= 100:
            if h % r == 0:
                print(nums2[3])
            else:
                print(nums2[h % r - 1])
        else:
            if pow(B, C) % r == 0:
                print(nums2[3])
            else:
                print(nums2[pow(B, C) - 1])
    else:
        if h % r == 0:
            print(nums2[3])
        else:
            print(nums2[h % r - 1])
