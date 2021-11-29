import io
import sys

# input here
_INPUT = """\
2
st

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
S = input()

def rle(s):
    tmp, count, ans = s[0], 1, []
    for i in range(1,len(s)):
        if tmp == s[i]:
            count += 1
        else:
            ans.append([tmp, count])
            tmp = s[i]
            count = 1
    ans.append([tmp, count])
    return ans

l = rle(S)

ans = 0
for _, count in l:
    if count > 1:
        ans += count * (count - 1) // 2

print(ans)
