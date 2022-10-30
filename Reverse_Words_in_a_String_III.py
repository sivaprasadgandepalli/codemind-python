n=input()
n=n.split()
for i in range(0,len(n)):
    s=n[i]
    n[i]=s[::-1]
n=' '.join(n)
print(n)
    