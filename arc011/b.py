import io
import sys

# input here
_INPUT = """\
4
aaa aa a aa

"""
sys.stdin = io.StringIO(_INPUT)



import re

N = int(input())
w = list(input().split())
w = [re.sub('[aiueoy,.]', '', word.lower()) for word in w]

dic = {'z': 0, 'r': 0, 'b': 1, 'c': 1, 'd': 2, 'w': 2, 't': 3, 'j': 3, 'f': 4, 'q': 4,
       'l': 5, 'v': 5, 's': 6, 'x': 6, 'p': 7, 'm': 7, 'h': 8, 'k': 8, 'n': 9, 'g': 9}

ans = []
for word in w:
    if word == '':
        continue
    num = ''
    for c in word:
        num += str(dic[c])
    ans.append(num)

print(*ans, sep=' ')
