import io
import sys

# input here
_INPUT = """\
1000 8
1 3 4 5 6 7 8 9

"""
sys.stdin = io.StringIO(_INPUT)



N, K = map(int, input().split())
D = list(map(int, input().split()))

for n in range(N, 10 ** 5):
    s = str(n)
    flag = True
    for i in s:
        if int(i) in D:
            flag = False
    if flag:
        print(n)
        break
