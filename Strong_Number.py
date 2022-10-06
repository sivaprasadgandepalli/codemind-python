def fact(n):
    s=1
    for i in range(1,n+1):
        s*=i
    return s
def stng(n):
    s=0
    org=n
    while(n>0):
        r=n%10
        s=s+fact(r)
        n=n//10
    if org==s:
        return True
    else:
        return False
n=int(input())
if(stng(n)):
    print("The number "+str(n)+" is a strong number")
else:
    print("The number "+str(n)+" is not a strong number")