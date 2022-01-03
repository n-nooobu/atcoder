import io
import sys

# input here
_INPUT = """\
tourist

"""
sys.stdin = io.StringIO(_INPUT)



S = input()

if S[-2:] == 'er':
    print('er')
else:
    print('ist')
