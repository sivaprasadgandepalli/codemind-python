def rev(n):
    s=0
    while n>0:
        r=n%10
        s=s*10+r
        n=n//10
    return s
def isadam(n):
    num=rev(n)
    sq1=n**2
    sq2=num**2
    if(sq1==rev(sq2)):
        return True
    else:
        return False

m=int(input())
if(isadam(m)):
    print("True")
else:
    print("False")