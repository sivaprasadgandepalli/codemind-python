n=input()
s=set(n)
s=''.join(sorted(s))
cnt=[]
for i in s:
    c=n.count(i)
    cnt.append(c)
d=cnt[0]
count=0
for i in cnt:
    if(i!=d):
        count+=1


    
if(count==0 or count==1):
    print("Valid String")
else:
    print("Not Valid")
