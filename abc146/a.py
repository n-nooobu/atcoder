import io
import sys

# input here
_INPUT = """\
SAT

"""
sys.stdin = io.StringIO(_INPUT)



S = input()

dic = {'SUN': 7, 'MON': 6, 'TUE': 5, 'WED': 4, 'THU': 3, 'FRI': 2, 'SAT': 1}
print(dic[S])
