s=input()
s=list(s)
k=input()
v=['a','e','i','o','u']
g=0
for i in range(0,len(s)):
    if k in v:
        if k in s:
            g=1
            c=s.index(k)
if g==0:
    print("False")
else:
    print("True")
    print(c)