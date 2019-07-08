def binary(n):
    res = ""
    while(n>0):
        res += str(n%2)
        n = n//2
    return res[::-1]

def octal(n):
    res = ""
    while(n>0):
        res += str(n%8)
        n = n//8
    return res[::-1]
    
def hexadecimal(n):
    res = ""
    alpha = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
    while(n>0):
        rem = n%16
        if(rem<=9):
            res += str(rem)
        else:
            res += alpha[rem]
        n = n//16
    return res[::-1]
    
n = int(input())
print(binary(n),octal(n),hexadecimal(n))
