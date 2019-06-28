def subsum(arr,s):
    if(s<0 or sum(arr)<s):
        return False
    if sum(arr)==s:
        return arr
    mem = [[False for i in range(s+1)]for i in range(len(arr))]
    for i in range(len(arr)):
        mem[i][0] = True
    j = 0
    for i in range(1,s+1):
        if(arr[j]==i):
            mem[j][i] = True
    for j in range(1,len(arr)):
        for i in range(1,s+1):
            if(i<arr[j]):
                mem[j][i] = mem[j-1][i]
            elif mem[j-1][i] == True:
                mem[j][i] = True
            else:
                mem[j][i] = mem[j-1][i-arr[j]] 
    if mem[len(arr)-1][s]:
        j = s
        i = len(arr)-1
        m = 0
        re = []
        while(j>0):
            if i==0:
                m = arr[i]
                re.append(arr[i])
                j = j-m
            if(mem[i][j] and mem[i-1][j]):
                i = i-1
                continue
            elif(mem[i][j] and mem[i-1][j]==False):
                re.append(arr[i])
                m = arr[i]
                i = i-1
                j = j-m
    return re
arr = sorted(list(map(int, input().split())))
s = int(input())
print(*subsum(arr,s),sep=" + ",end="")
print(" = "+str(s))
