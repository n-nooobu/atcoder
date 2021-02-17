import io
import sys

# input here
_INPUT = """\
999999999

"""
sys.stdin = io.StringIO(_INPUT)



from collections import deque, Counter

N = int(input())

q = deque([0])
ans = 0
while q:
    t = q.pop()
    if t == 0:
        for i in [3, 5, 7]:
            q.append(i)
    else:
        for i in [3, 5, 7]:
            t2 = t + i * 10 ** len(str(t))
            if t2 > N:
                continue
            q.append(t2)

            c = Counter(str(t2))
            if c['3'] and c['5'] and c['7']:
                ans += 1

print(ans)
