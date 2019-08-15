n = int(input())
arr = list(map(int, input().split()))
inc = 0
exc = 0
for i in arr:
    new_exc = max(inc,exc)
    inc = exc + i
    exc = new_exc
print(max(inc,exc))
