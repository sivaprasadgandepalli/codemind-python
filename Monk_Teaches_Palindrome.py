def pal(n):
    s=n[::-1]
    if(s==n):
        return True
    else:
        return False

n=int(input())
for i in range(1,n+1):
    s=input()
    if(pal(s) and len(s)%2==0):
        print("YES EVEN")
    elif(pal(s) and len(s)%2!=0):
        print("YES ODD")
    else:
        print("NO")