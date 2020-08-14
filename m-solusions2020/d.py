N = int(input())
A = list(map(int, input().split()))

money = 1000
stock = 0
for day in range(N):
    if day == N - 1:
        money += stock * A[day]
        stock = 0
    elif A[day] == A[day+1]:
        continue
    elif A[day] < A[day+1]:
        stock += money // A[day]
        money = money % A[day]
    elif A[day] > A[day+1]:
        money += stock * A[day]
        stock = 0

print(money)
