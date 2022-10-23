n=input()
mx=" "
mn=0
for i in range(0,len(n)):
    if(ord(n[i])>mn):
        mn=ord(n[i])
        mx=n[i]
print(mx)