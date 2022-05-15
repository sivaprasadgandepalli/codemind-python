def prime_fact(n):
    s=[]
    t=2
    i=0
    while True:
        if n%t==0:
            n=n//t
            s.append(t)
        else:
            t+=1
        if n<t:
            break
    i+=1
    return s
n=int(input())
s1=prime_fact(n)
h=0
for i in range(0,len(s1)):
    for j in range(i+1,len(s1)):
        if s1[i]*s1[j]==n:
            print(s1[i],s1[j])
            h=1
            break
if h==0:
    print(-1)
    
       
