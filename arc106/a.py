import io
import sys

# input here
_INPUT = """10460353208


"""
sys.stdin = io.StringIO(_INPUT)



import sys
N = int(input())

for i in range(1, 100):
    for j in range(1, 100):
        if 3 ** i + 5 ** j == N:
            print(i, j)
            sys.exit()

print(-1)
