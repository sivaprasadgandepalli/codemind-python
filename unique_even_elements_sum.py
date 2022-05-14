n=int(input())
d=list(map(int,input().split()))
s=[]
ec=0
for i in range(0,len(d)):
    if d[i] not in s:
        s.append(d[i])
    else:
        s=s
for i in range(0,len(s)):
    if s[i]%2==0:
        ec+=s[i]
print(ec)        