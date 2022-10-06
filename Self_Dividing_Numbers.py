def sdn(n):
    c=0
    s=0
    org=n
    while(n>0):
        r=n%10
        s+=1
        if(r>0):
            if (org%r==0):
                c+=1
        n=n//10
    if(s==c):
        return True
    else:
        return False
m=int(input())
n=int(input())
for i in range(m,n+1):
    if(sdn(i)):
        print(i,end=" ")