import io
import sys

# input here
_INPUT = """\
DULL


"""
sys.stdin = io.StringIO(_INPUT)



S = input()

for i in range(len(S)):
    if (i + 1) % 2 == 1:
        if S[i] == 'L':
            print('No')
            exit()
    else:
        if S[i] == 'R':
            print('No')
            exit()
print('Yes')
