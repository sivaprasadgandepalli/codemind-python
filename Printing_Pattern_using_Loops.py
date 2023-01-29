n=int(input())
top=0
down=2*n-2
left=0
right=2*n-2
for i in range(0,2*n-1):
    for j in range(0,2*n-1):
        k=min(min(i-top,down-i),min(j-left,right-j))
        print(n-k,end=" ")
    print()