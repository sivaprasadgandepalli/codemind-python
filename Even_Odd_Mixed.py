n=int(input())
es=0
os=0
l=0
while(n>0):
    r=n%10
    l+=1
    if(r%2==0):
        es+=1
    else:
        os+=1
    n=n//10
if(es==l):
    print("Even")
elif(os==l):
    print("Odd")
else:
    print("Mixed")