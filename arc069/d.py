import io
import sys

# input here
_INPUT = """\

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
s = input()

for animals in ['SS', 'SW', 'WS', 'WW']:
    for i in range(1, N):
        if animals[-1] == 'S':
            if s[i] == 'o':
                animals.append('')
