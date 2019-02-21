#https://www.hackerrank.com/challenges/separate-the-numbers/problem

for _ in range(int(input())):
    a = input()
    f = 0
    if a == a[0]:
        print("NO")
    else:
        for i in range(1,len(a)):
            x = []
            x.append(a[:i])
            while(len(''.join(x))<len(a)):
                x.append(str(int(x[-1])+1))
            if ''.join(x) == str(a):
                print("YES",end=" ")
                print(x[0])
                f = 0
                break
            else:
                f = 1
    if(f==1):
        print("NO")
