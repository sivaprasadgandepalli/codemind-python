m=int(input())
a=0
b=1
s=0
for i in range (1,m-1):
    c=a+b
    if(c==m):
       s+=1 
    a=b
    b=c
if(s==0):
    print("False")
else:
    print("True")