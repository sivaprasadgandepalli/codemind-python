def fs(n):
    s=0
    for i in range(1,(n//2)+1):
        if(n%i==0):
            s=s+i
    return s

n=int(input())
m=int(input())
if(fs(n)==m and fs(m)==n):
    print("Amicable")
else:
     print("Not Amicable")
        