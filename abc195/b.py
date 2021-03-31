import io
import sys

# input here
_INPUT = """\
1 1 1


"""
sys.stdin = io.StringIO(_INPUT)



A, B, W = map(int, input().split())
W *= 1000
ans = 0

if A == B:
    if W % A == 0:
        print(W // A, W // A)
    else:
        print('UNSATISFIABLE')
else:
    n_min = W // A
    if (W - A * n_min) % (B - A) == 0:
        if (W - A * n_min) // (B - A) <= n_min:
            ans_min = n_min
        else:
            ans = 'UNSATISFIABLE'
    else:
        if (W - A * n_min) // (B - A) < n_min:
            ans_min = n_min
        else:
            ans = 'UNSATISFIABLE'

    if W % B == 0:
        n_max = W // B
    else:
        n_max = W // B + 1
    if (B * n_max - W) % (B - A) == 0:
        if (B * n_max - W) // (B - A) <= n_min:
            ans_max = n_max
        else:
            ans = 'UNSATISFIABLE'
    else:
        if (B * n_max - W) // (B - A) < n_max:
            ans_max = n_max
        else:
            ans = 'UNSATISFIABLE'

    if ans:
        print(ans)
    else:
        print(n_max, n_min)
