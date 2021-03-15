import math

T = int(input())

res = []
for i in range(T):
    N, K = map(int, input().split(' '))

    li = list(map(int, input().split(' ')))
    dist_list = []
    for j in range(1, len(li)):
        dist = li[j]-li[j-1]
        if dist > 1:
            dist_list.append(li[j]-li[j-1])

    min_dist = 1
    max_dist = max(dist_list)
    mid = math.floor((min_dist+max_dist) / 2)
    answer = mid
    while min_dist <= max_dist:
        mid = math.floor((min_dist+max_dist) / 2)

        number_of_sessions = 0
        for dist in dist_list:
            if dist > mid:
                number_of_sessions += math.ceil(dist/mid) - 1
        if number_of_sessions <= K:
            answer = mid
        if number_of_sessions > K:
            min_dist = mid + 1
        else:
            max_dist = mid - 1
    
    
    res.append("Case #{}: {}".format(i+1,answer))


for i in res:
    print(i)