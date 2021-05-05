import io
import sys

# input here
_INPUT = """\
31
puvxlhwva
fubxha
tbxvtralb
jnerjnerun
xvzvgnpuvgb
lhxban
xnaxrvjb
xvmhxhgnzr
xbabubfuvav
lnggrxvgn
fnffbxhqntn
lhxbab
fuvehfuvgbfvgr
chermragbjb
bartnvfuvgnv
ranwvqbevaxh
mbar
jb
whaovfuvgr
ubfuvvabqn
xbabartnvjb
xnanrgrxhereron
bgbanfuvxh
xbabubfuvjb
ngbavfhehgfhzbevqn
jnerjnerun
nenfbvtbgbjb
abmbznanv
znrzhxvan
urawvjb
xvgnvfuvgrveh
"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())

for i in range(N):
    S = input()
    n = [chr(ord(s)+13) if ord(s)+13 < ord('a')+26 else chr(ord(s)-13) for s in S]
    print(''.join(n))
