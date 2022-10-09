def prop(n):
    sum=0
    for i in range(1,n):
        if(n%i==0):
            sum+=i
    return sum
    
m=int(input())
if(prop(m)>m):
    print("True")
else:
    print("False")