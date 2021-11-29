import io
import sys

# input here
_INPUT = """\
.#
#.

"""
sys.stdin = io.StringIO(_INPUT)



S1 = input()
S2 = input()

if (S1[0] == '.' and S1[1] == '#' and S2[0] == '#' and S2[1] == '.') or (S1[0] == '#' and S1[1] == '.' and S2[0] == '.' and S2[1] == '#'):
    print('No')
else:
    print('Yes')

