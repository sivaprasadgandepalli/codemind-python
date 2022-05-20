def vo_count(s):
    v="aeiouAEIOU"
    c=0
    for i in s:
        if i in v:
            c+=1
    return c
s=input()
s=s.split()
n=[]
c1=0
for i in s:
    n.append(vo_count(i))
for i in n:
    if i==min(n):
        c1+=1
print(c1)
