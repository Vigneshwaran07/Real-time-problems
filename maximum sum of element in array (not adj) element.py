a = list(map(int, input().split()))
inc = 0
exc = 0
for i in range(len(a)):
    t = max(inc,exc)
    inc = exc+a[i]
    exc = t
print(max(inc,exc))
