m,n=map(int,input().split())
mx=max(m,n)
mn=min(m,n)
i=1
while True:
    if(mx*i%mn==0):
        print(mx*i)
        break
    i+=1
        