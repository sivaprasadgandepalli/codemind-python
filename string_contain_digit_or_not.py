n=input()
c=0
for i in n:
    if(i.isdigit()):
        c+=1
if(c==0):
    print("Doesn't contain digit")
else:
    print("Contains "+str(c)+" digit")