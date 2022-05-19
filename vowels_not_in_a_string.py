n=input()
s=list(n)
v=['a','e','i','o','u']
c=[]
c1=[]
for i in s:
    if i in v:
        c.append(i)
for i in v:
    if i not in c:
        c1.append(i)
if len(c1)==0:
    print(0)
else:
    print(*c1)
