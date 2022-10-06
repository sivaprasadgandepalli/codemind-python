def fact(n):
    sum=1;
    for i in range(1,n+1):
        sum=sum*i;
    return sum

n=int(input())
s=[]
for i in range(0,n):
    v=int(input())
    s.append(fact(v))
for i in s:
    print(i)
