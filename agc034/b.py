import io
import sys

# input here
_INPUT = """\
ABCACCBABCBCAABCB

"""
sys.stdin = io.StringIO(_INPUT)



s = input()

n_state = True
a_state = False
ab_state = False
abc_state = False
abcb_state = False
a_cnt = 0
bc_cnt = 0
ans = 0
for i in s:
    if n_state:
        if i == 'A':
            n_state = False
            a_state = True
    elif a_state:
        if i == 'A':
            a_cnt += 1
        if i == 'B':
            a_state = False
            ab_state = True
        if i == 'C':
            a_cnt = 0
            a_state = False
            n_state = True
    elif ab_state:
        if i == 'A':
            ab_state = False
            a_state = True
        if i == 'B':
            ab_state = False
            n_state = True
        if i == 'C':
            ab_state = False
            abc_state = True
    elif abc_state:
        if i == 'A':
            abc_state = False
            a_state = True
            ans += a_cnt + bc_cnt + 1
            a_cnt += 1
            bc_cnt = 0
        if i == 'B':
            abc_state = False
            abcb_state = True
        if i == 'C':
            abc_state = False
            n_state = True
            ans += a_cnt + bc_cnt + 1
            a_cnt = 0
            bc_cnt = 0
    elif abcb_state:
        if i == 'A':
            abcb_state = False
            a_state = True
            ans += a_cnt + bc_cnt + 1
            a_cnt = 0
            bc_cnt = 0
        if i == 'B':
            abcb_state = False
            n_state = True
            ans += a_cnt + bc_cnt + 1
            a_cnt = 0
            bc_cnt = 0
        if i == 'C':
            abcb_state = False
            abc_state = True
            bc_cnt += 1
if abc_state or abcb_state:
    ans += a_cnt + bc_cnt + 1

print(ans)
