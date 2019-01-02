a = list(map(int, input().split()))
inc = 0
ex = 0
for i in a:
  nex = max(inc,ex)
  inc = ex + i
  ex = nex
print(max(inc,ex))  
