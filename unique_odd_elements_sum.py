n=int(input())
d=list(map(int,input().split()))
s=[]
os=0
for i in range(0,len(d)):
    if d[i] not in s:
        s.append(d[i])
    else:
        s=s
for i in range(0,len(s)):
    if s[i]%2:
        os+=s[i]
print(os)        