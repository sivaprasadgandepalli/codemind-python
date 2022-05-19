def rev(s):
    c=s[::-1]
    return c
n=input()
n=n.split()
k=[]
for i in n:
    g=n.index(i)
    if g%2==0:
        k.append(rev(i))
    else:
        k.append(i)
print(' '.join(k))
    
