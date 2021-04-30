import io
import sys

# input here
_INPUT = """\
RRRLLRLLRRRLLLLL


"""
sys.stdin = io.StringIO(_INPUT)



S = input()

ans = [0] * len(S)
r_flag = False
l_flag = False
r = 0
l = 0
for i, s in enumerate(S):
    if r_flag and l_flag:
        if s == 'R':
            l_flag = False
            ans[i-(l+1)] = r // 2 + r % 2 + l // 2
            ans[i-l] = l // 2 + l % 2 + r // 2
            r = 1
            l = 0
        else:
            l += 1
    elif r_flag:
        if s == 'R':
            r += 1
        else:
            l_flag = True
            l += 1
    else:
        if s == 'R':
            r_flag = True
            r += 1
ans[len(S)-(l+1)] = r // 2 + r % 2 + l // 2
ans[len(S)-l] = l // 2 + l % 2 + r // 2

for a in ans:
    print(a, end=' ')
