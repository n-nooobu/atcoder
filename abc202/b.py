import io
import sys

# input here
_INPUT = """\
86910


"""
sys.stdin = io.StringIO(_INPUT)



S = input()

for i in range(len(S) - 1, -1, -1):
    if S[i] == '0':
        print('0', end='')
    elif S[i] == '1':
        print('1', end='')
    elif S[i] == '6':
        print('9', end='')
    elif S[i] == '8':
        print('8', end='')
    else:
        print('6', end='')
