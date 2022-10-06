def add(n):
    s=0
    while(n>0):
        r=n%10
        s+=r
        n=n//10
    return s
n=int(input())
s=add(n)
while(s>10):
    s=add(s)
print(s)