import io
import sys

# input here
_INPUT = """\
1000000000000

"""
sys.stdin = io.StringIO(_INPUT)



import sys

H = int(input())

ans = [1] * 50
two = [1] * 50
for i in range(1, 50):
    ans[i] = ans[i - 1] * 2 + 1
    two[i] = two[i - 1] * 2

for i in range(1, 50):
    if H < two[i]:
        print(ans[i - 1])
        sys.exit()
