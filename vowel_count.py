n=input()
s=list(n)
c=0
vo="aeiouAEIOU"
for i in s:
    if i in vo:
        c+=1
print(c)