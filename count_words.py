s=input()
s=s.split()
c=0
v="aeiouAEIOU"
for i in s:
    k=list(i)
    if k[0] in v:
        if k[-1] not in v:
            c+=1
print(c)            