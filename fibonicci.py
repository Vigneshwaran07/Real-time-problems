#series 1 1 2 3 5 8.....

import math
n=int(input("Enter number"))
phi=(1+math.sqrt(5))/2
phin=(1-math.sqrt(5))/2
fibo=((phi**n)-(phin**n))/math.sqrt(5)
print(fibo)
