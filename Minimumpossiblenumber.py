a = input()
b = input()
c = a+b
mini = 0
even = []
ec = 0
for ind,i in enumerate(c):
    if(int(i)%2==0):
        ec += 1
    if ec>=2:
        break
if(ec<2):
    print(-1)
else:
    list1 = sorted(list(map(int, list(c))))
    if(min(list1)==0):
        mini = min(list(map(int, c.replace('0',''))))
    else:
        mini = min(list1)
    del list1[list1.index(mini)]
    list1 = [mini]+list1
    for ind,i in enumerate(list1[::-1]):
        if(i%2==0):
            even.append([i,list1.index(i)])
        if(len(even)==2):
            break
    del list1[even[0][1]]
    del list1[even[1][1]]
    list1 = list1+[even[1][0]]+[even[0][0]]
    print(''.join(map(str,list1)))
    
