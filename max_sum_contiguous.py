arr = list(map(int, input().split(',')))
max_global = max_current = arr[0]
for i in range(1, len(arr)):
    max_current = max(arr[i], max_current + arr[i])
    max_global = max(max_current, max_global)
print(max_global)
