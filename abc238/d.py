import io
import sys

# input here
_INPUT = """\
2
1 8
4 2

"""
sys.stdin = io.StringIO(_INPUT)



T = int(input())

for t in range(T):
    a, s = map(int, input().split())
    a = bin(a)[2:].zfill(61)[::-1]
    slen = len(bin(s)[2:])
    s = bin(s)[2:].zfill(61)[::-1]
    k = False
    flg = True
    for i in range(61):
        if not k:
            if a[i] == '1' and s[i] == '1':
                print('No')
                flg = False
                break
            if a[i] == '1' and s[i] == '0':
                k = True
        else:
            if a[i] == '1' and s[i] == '0':
                print('No')
                flg = False
                break
            if a[i] == '0' and s[i] == '1':
                k = False
            if i >= slen:
                print('No')
                flg = False
                break
    if flg:
        print('Yes')
