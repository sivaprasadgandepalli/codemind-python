def ssq(n):
    s=0
    while (n>0):
       r=n%10
       s+=r**2
       n=n//10
    return s

n=int(input())
ca=ssq(n)
while(ca>=10):
    ca=ssq(ca)
if(ca==1 or ca==7):
    print("True")
else:
    print("False")
    