def rev(s):
    c=s[::-1]
    return c
s=input()
s=s.split()
l=len(s)
k=[]
for i in range((l-1),-1,-1):
    k.append(rev(s[i]))
print(' '.join(k))
    
