from collections import deque

N, K = map(int, input().split())
A = list(map(int, input().split()))

A_p = [i for i in A if i >= 0]
A_n = [i for i in A if i < 0]
if A_p:
    A_p.sort()
    A_p.reverse()
if A_n:
    A_n.sort()
    A_n.reverse()
A_p = deque(A_p)
A_n = deque(A_n)

ans = 1
mod = 10 ** 9 + 7
if len(A_p) == 0 and K % 2 != 0:
    while K != 0:
        ans = ans * A_n[0] % mod
        A_n.popleft()
        K -= 1
elif K % 2 != 0:
    while K != 0:
        if len(A_p) >= 2 and len(A_n) >= 2:
            if A_p[0] * A_p[1] > A_n[0] * A_n[1]:
                ans = ans * A_p[0] * A_p[1] % mod
                A_p.popleft()
                A_p.popleft()
            else:
                ans = ans * A_n[0] * A_n[1] % mod
                A_n.popleft()
                A_n.popleft()
        elif len(A_p) >= 2:
            ans = ans * A_p[0] * A_p[1] % mod
            A_p.popleft()
            A_p.popleft()
        elif len(A_n) >= 2:
            ans = ans * A_n[0] * A_n[1] % mod
            A_n.popleft()
            A_n.popleft()
        K -= 2
else:
    while K > 1:
        if len(A_p) >= 2 and len(A_n) >= 2:
            if A_p[0] * A_p[1] > A_n[0] * A_n[1]:
                ans = ans * A_p[0] * A_p[1] % mod
                A_p.popleft()
                A_p.popleft()
            else:
                ans = ans * A_n[0] * A_n[1] % mod
                A_n.popleft()
                A_n.popleft()
        elif len(A_p) >= 2:
            ans = ans * A_p[0] * A_p[1] % mod
            A_p.popleft()
            A_p.popleft()
        elif len(A_n) >= 2:
            ans = ans * A_n[0] * A_n[1] % mod
            A_n.popleft()
            A_n.popleft()
        K -= 2
    ans = ans * A_p[0] % mod

print(ans)
