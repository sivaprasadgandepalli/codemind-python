s=input()
s=list(s)
sp=0
for i in range(len(s)):
    if s[i]==" " :
        sp=sp
    elif s[i].isalpha():
        sp=sp
    else:
        sp+=1
print(sp)