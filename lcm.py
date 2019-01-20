from math import gcd
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    lcm = a[0]
    for i in a[1:]:
        lcm = lcm*i//gcd(lcm, i)
    print(lcm)    
