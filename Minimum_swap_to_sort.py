arr = [1, 5, 4, 3, 2]
arr_ind = sorted([*enumerate(arr)], key = lambda it:it[1])
visit = {i:False for i in range(len(arr))}
answer = 0
for i in range(len(arr)):
    j = i
    temp = 0
    if(i == arr_ind[i][0] or visit[i]):
        continue
    else:
        while not visit[j]:
            visit[j] = True
            temp += 1
            j = arr_ind[j][0]
        if(temp>0):
            answer += temp - 1
print(answer)
