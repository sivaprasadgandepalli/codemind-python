n=int(input())
d=list(map(int,input().split()))
es=0
os=0
for i in range(0,len(d)):
    if i%2==0:
        es+=d[i]
    else:
        os+=d[i]
        
if(abs(es-os)%4==0):
    print("X")
else:
    print("Y")