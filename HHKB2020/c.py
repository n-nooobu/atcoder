import io
import sys

# input here
_INPUT = """\
4
1 1 0 2

"""
sys.stdin = io.StringIO(_INPUT)



from collections import OrderedDict

N = int(input())
p = list(map(int, input().split()))

dic = OrderedDict()
for i in range(2 * 10 ** 5 + 5):
    dic[str(i)] = i

for i in range(N):
    try:
        del dic[str(p[i])]
    except KeyError:
        pass
    for j in dic.items():
        print(j[1])
        break
