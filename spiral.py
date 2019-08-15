n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
i = 0
j = 0
down = 1
top = 0
left = 0
right = 0
result = []
result += arr[0]
del arr[0]

while(len(arr)>=1):
    if down == 1:
        for i in range(len(arr)):
            result.append(arr[i][-1])
            del arr[i][-1]
        down = 0
        left = 1
    if left == 1:
        result += arr[len(arr)-1][::-1]
        del arr[len(arr)-1]
        left = 0
        top = 1
    if top == 1:
        for i in range(len(arr)-1,0,-1):
            result.append(arr[i][0])
            del arr[i][0]
        top = 0
        right = 1
    if right == 1 and len(arr)>0:
        result + = arr[0]
        del arr[0]
        right = 0
        down = 1
print(*result)
