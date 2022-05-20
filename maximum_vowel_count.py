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
for i in s:
    n.append(vo_count(i))
print(max(n))
