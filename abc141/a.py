import io
import sys

# input here
_INPUT = """\

"""
sys.stdin = io.StringIO(_INPUT)



S = input()

if S == 'Sunny':
    print('Cloudy')
elif S == 'Cloudy':
    print('Rainy')
else:
    print('Sunny')
