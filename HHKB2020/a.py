import io
import sys

# input here
_INPUT = """\
Y
a

"""
sys.stdin = io.StringIO(_INPUT)



S = input()
T = input()

if S == 'Y':
    if T == 'a':
        print('A')
    elif T == 'b':
        print('B')
    else:
        print('C')
else:
    print(T)
