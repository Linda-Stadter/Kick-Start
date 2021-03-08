import math
from collections import defaultdict

def get_max_beauty(stack, K, remaining):
    if stack < 0 or remaining <= 0:
        return 0

    if dp_table[stack][remaining] != -1:
        return dp_table[stack][remaining]

    max_beauty = get_max_beauty(stack-1, K, remaining)

    for i in range(0, min(remaining,K)):
        max_beauty = max(max_beauty, value_table[stack][i] + get_max_beauty(stack-1, K, remaining-1-i))
        
    dp_table[stack][remaining] = max_beauty
    return max_beauty

T = int(input())

res = []
value_table = []
dp_table = []
for i in range(T):
    N, K, P = map(int, input().split(' '))

    values = []
    weights = []
    
    for j in range(N):
        li = list(map(int, input().split(' ')))
        stack_list = []
        
        for v in range(1, len(li)+1):
           stack_list.append(sum(li[:v]))
        value_table.append(stack_list)

    dp_table = defaultdict(lambda: defaultdict(lambda: -1))
    res.append("Case #{}: {}".format(i+1,get_max_beauty(N-1, K, P)))
    value_table = []


for i in res:
    print(i)
