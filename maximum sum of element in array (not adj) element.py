n = int(input())
arr = list(map(int, input().split()))
inc = 0
exc = 0
for i in arr:
    temp = inc
    inc = max(inc, exc+i)
    exc = temp
print(max(inc,exc))
