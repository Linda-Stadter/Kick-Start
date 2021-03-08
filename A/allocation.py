T = int(input())

res = []
for i in range(T):
    N, B = map(int, input().split(' '))
    l = map(int, input().split(' '))

    cost = 0
    for num, house in enumerate(sorted(l)):
        cost += house
        if cost > B:
            res.append("Case #{}: {}".format(i+1,num))
            break
        
    if cost <= B:
        res.append("Case #{}: {}".format(i+1,N))

for i in res:
    print(i)
