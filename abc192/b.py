import io
import sys

# input here
_INPUT = """\
a

"""
sys.stdin = io.StringIO(_INPUT)



S = input()

flag = True
for i, s in enumerate(S):
    if i % 2 == 0:
        if not s.islower():
            flag = False
    else:
        if s.islower():
            flag = False

if flag:
    print('Yes')
else:
    print('No')
