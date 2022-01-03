import io
import sys

# input here
_INPUT = """\
2

"""
sys.stdin = io.StringIO(_INPUT)



K = int(input())

ans = []
d = K % 50
a = K // 50
for i in range(50):
    if i < 50 - d:
        ans.append(49 - d)
    else:
        ans.append(50)
    ans[-1] += a

print(50)
print(*ans, sep=' ')
