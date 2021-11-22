import io
import sys

# input here
_INPUT = """\
5
666 777 888 777 666

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
S = list(map(int, input().split()))

ans = 0
for i in range(N):
    flag = False
    for a in range(1, 143):
        for b in range(1, 143):
            if S[i] == 4 * a * b + 3 * a + 3 * b:
                flag = True
    if not flag:
        ans += 1

print(ans)
