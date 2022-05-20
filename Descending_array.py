n=int(input())
d=list(map(int,input().split()))
s=[]
for i in d:
    if i not in s:
        s.append(i)
s.sort()
if s[::-1]==d:
    print("yes")
else:
    print("no")