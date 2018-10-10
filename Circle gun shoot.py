li = list(range(1, int(input("Enter the number of person :"))+1))
i = 0
while (True):
    if len(li) == 1:
        print(int(li[0]))
        break
    if i == len(li) - 1:
        i = 0
        del li[i]
        continue
    if i == len(li):
        i = 1
        del li[i]
        continue

    i = i + 1
    del li[i]


