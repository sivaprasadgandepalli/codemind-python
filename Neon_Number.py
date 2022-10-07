N=int(input())
nm=N**2
sum=0
while nm>0:
    sum=sum+(nm%10)
    nm=nm//10
if N==sum:
    print("Neon Number")
else:
    print("Not Neon Number")
