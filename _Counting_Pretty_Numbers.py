n=int(input())
for i in range(1,n+1):
    m,n=map(int,input().split())
    c=0
    for i in range(m,n+1):
        r=i%10
        if(r==2 or r==3 or r==9):
            c+=1
    print(c)