def rev(s):
    c=s[::-1]
    return c
n=input()
n=n.split()
k=[]
for i in n:
    k.append(rev(i))
print(' '.join(k))
    
