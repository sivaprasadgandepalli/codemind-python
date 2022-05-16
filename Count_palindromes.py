def palindrome(n):
    string=str(n)
    string=list(string)
    string.reverse()
    string=''.join(string)
    num=int(string)
    if n==num:
        return True
    else:
        return False
n=int(input())    
d=list(map(int,input().split()))
c=0
for i in range(0,len(d)):
    if palindrome(d[i]):
        c+=1
print(c)