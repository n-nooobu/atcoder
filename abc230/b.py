import io
import sys

# input here
_INPUT = """\
oxxx

"""
sys.stdin = io.StringIO(_INPUT)



import sys

S = input()

cnt = 0
start = 1
for i in range(len(S)):
    if S[i] == 'o':
        if start:
            cnt = 0
            start = 0
        else:
            if cnt != 2:
                print('No')
                sys.exit()
            else:
                cnt = 0
    else:
        cnt += 1
        if cnt > 2:
            print('No')
            sys.exit()

print('Yes')
