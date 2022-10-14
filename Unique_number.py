n=int(input())
s1=list(str(n))
s2=set(str(n))
if(len(s1)==len(s2)):
    print("Unique Number")
else:
    print("Not Unique Number")