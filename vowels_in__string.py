s=input()
s=list(s)
v1=['a','e','i','o','u']
v2=['A','E','I','O','U']
s1=[]
g=0
for i in s:
    if i in v1:
        if i not in s1:
            s1.append(i)
            g=1
    elif i in v2:
        if i not in s1:
            s1.append(i)
 
if g==1:
    print(*s1)
else:
    print(-1)