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
s=[]
for i in range(1,t+1):
    v=int(input())
    s.append(v)
for i in s:
    if ispal(i):
        print("True")
    else:
        print("False")
    