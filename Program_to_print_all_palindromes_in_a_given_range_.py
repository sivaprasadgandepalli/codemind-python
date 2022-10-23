def ispal(n):
    org=n
    s=0
    while n>0:
        r=n%10
        s=s*10+r
        n=n//10
    if(s==org):
        return True
    else:
        return False
m=int(input())
n=int(input())
for i in range(m,n+1):
    if(ispal(i)):
        print(i,end=" ")