from sys import maxsize
#arr = list(map(int, input().split(',')))
arr =[-2, -5, 6, -2, -3, 1, 5, -6]
max = -maxsize
max_current = max_global = 0
for i in range(0, len(arr)):
    max_current = max_global + arr[i]
    if max_global < max_current:
        max_global = max_current
print(max_global)
