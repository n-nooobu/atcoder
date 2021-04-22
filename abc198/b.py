import io
import sys

# input here
_INPUT = """\
123456789


"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())

def is_kaibun(sx):
    if sx[:len(sx) // 2] == sx[::-1][:len(sx) // 2]:
        return True
    else:
        return False

sn = str(N)
for i in range(10):
    if is_kaibun(sn):
        print('Yes')
        exit()
    sn = '0' + sn

print('No')
