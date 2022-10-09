def ispal(n):
    s=0
    org=n
    while n>0:
        r=n%10
        s=s*10+r
        n=n//10
    if(org==s):
        return True
    else:
        return False

t=int(input())
if ispal(t):
    print("True")
else:
    print("False")