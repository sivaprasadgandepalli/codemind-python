s=input()
s=list(s)
v1=['a','e','i','o','u']
v2=['A','E','I','O','U']
s1=[]
s2=[]
for i in s:
    if i in v1:
        if i not in s1:
            s1.append(i)
    elif i in v2:
        if i not in s2:
            s2.append(i)
if len(s1)==len(v1):
    print("True")
elif len(s2)==len(v2):
    print("True")
else:
    print("False")
