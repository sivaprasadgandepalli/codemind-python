N=int(input())
m=N
sum=0
i=0
while N:
    d=N%10
    N=N//10
    sum+=d
    i+=1
if m%sum==0:
    print("True")
else:
    print("False")