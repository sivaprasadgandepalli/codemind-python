l=int(input())
n=int(input())
s=[]
for i in range(0,n):
    m,n=map(int,input().split())
    if(m<l or n<l):
        s.append("UPLOAD ANOTHER")
    else:
        if(m==n):
            s.append("ACCEPTED")
        else:
            s.append("CROP IT")
for i in s:
    print(i)