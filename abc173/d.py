N = int(input())
A = list(map(int, input().split()))

A.sort()
A.reverse()

list = []
ans = 0
list.append(A[0])
for i in range(1, len(A)):
        ans += list[i - 1]
        list.append(A[i])
        list.append(A[i])

print(ans)
