n=int(input())
for i in range(1,n+1):
    v=input()
    c=0
    for j in v:
        if(j.isnumeric()):
            c+=1
    if(c==0):
        print("No")
    else:
        print("Yes")