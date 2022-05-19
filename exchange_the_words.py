s=input()
s=s.split()
l=len(s)
k=[]
for i in range((l-1),-1,-1):
    k.append(s[i])
print(' '.join(k))
    
