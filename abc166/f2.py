import io
import sys

# input here
_INPUT = """\
1 0 9 0
AC
"""
sys.stdin = io.StringIO(_INPUT)



import sys

N, A, B, C = map(int, input().split())
s = [input() for _ in range(N)]

ans = []
if A + B + C == 0:
    print('No')
elif A + B + C == 1:
    for i in range(N):
        if s[i] == 'AB':
            if A == 0 and B == 0:
                print('No')
                sys.exit()
            elif A == 0:
                B -= 1
                A += 1
                ans.append('A')
            else:
                A -= 1
                B += 1
                ans.append('B')
        elif s[i] == 'AC':
            if A == 0 and C == 0:
                print('No')
                sys.exit()
            if A == 0:
                C -= 1
                A += 1
                ans.append('A')
            else:
                A -= 1
                C += 1
                ans.append('C')
        else:
            if B == 0 and C == 0:
                print('No')
                sys.exit()
            if B == 0:
                C -= 1
                B += 1
                ans.append('B')
            else:
                B -= 1
                C += 1
                ans.append('C')
    print('Yes')
    for i in range(N):
        print(ans[i])
else:
    if N == 1:
        if s[0] == 'AB' and A == 0 and B == 0:
            print('No')
            sys.exit()
        elif s[0] == 'AC' and A == 0 and C == 0:
            print('No')
            sys.exit()
        elif s[0] == 'BC' and B == 0 and C == 0:
            print('No')
            sys.exit()
    for i in range(N - 1):
        if s[i] == 'AB':
            if A == 0 and B == 0:
                print('No')
                sys.exit()
            elif A == 0:
                B -= 1
                A += 1
                ans.append('A')
            elif B == 0:
                A -= 1
                B += 1
                ans.append('B')
            else:
                if s[i + 1] == 'AB':
                    A -= 1
                    B += 1
                    ans.append('B')
                elif s[i + 1] == 'AC':
                    B -= 1
                    A += 1
                    ans.append('A')
                else:
                    A -= 1
                    B += 1
                    ans.append('B')
        elif s[i] == 'AC':
            if A == 0 and C == 0:
                print('No')
                sys.exit()
            elif A == 0:
                C -= 1
                A += 1
                ans.append('A')
            elif C == 0:
                A -= 1
                C += 1
                ans.append('C')
            else:
                if s[i + 1] == 'AC':
                    A -= 1
                    C += 1
                    ans.append('C')
                elif s[i + 1] == 'AB':
                    C -= 1
                    A += 1
                    ans.append('A')
                else:
                    A -= 1
                    C += 1
                    ans.append('C')
        else:
            if B == 0 and C == 0:
                print('No')
                sys.exit()
            elif B == 0:
                C -= 1
                B += 1
                ans.append('B')
            elif C == 0:
                B -= 1
                C += 1
                ans.append('C')
            else:
                if s[i + 1] == 'BC':
                    C -= 1
                    B += 1
                    ans.append('B')
                elif s[i + 1] == 'AB':
                    C -= 1
                    B += 1
                    ans.append('B')
                else:
                    B -= 1
                    C += 1
                    ans.append('C')
    print('Yes')
    for i in range(N - 1):
        print(ans[i])
    if s[-1] == 'AB':
        if A == 0:
            print('A')
        elif B == 0:
            print('B')
        else:
            print('A')
    elif s[-1] == 'AC':
        if A == 0:
            print('A')
        elif C == 0:
            print('C')
        else:
            print('A')
    else:
        if B == 0:
            print('B')
        elif C == 0:
            print('C')
        else:
            print('B')
