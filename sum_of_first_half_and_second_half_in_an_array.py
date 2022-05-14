n=int(input())
d=list(map(int,input().split()))
s1=0
s2=0
for i in range(0,n//2):
    s1+=d[i]
for j in range(n//2,n):
    s2+=d[j]
print(s1)
print(s2)
