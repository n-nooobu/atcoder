import io
import sys

# input here
_INPUT = """\
84939825309432908832902189.9092309409809091329

"""
sys.stdin = io.StringIO(_INPUT)



X = input()

for i in range(len(X)):
    if X[i] == '.':
        print(X[:i])
        exit()

print(X)
