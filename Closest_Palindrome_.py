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
s=[]
i=0
while True:
    if palindrome(i):
        s.append(i)
    if i>n:
        if palindrome(i):
            break
    i+=1
if n not in s:
    d1=s[-1]
    d2=s[-2]
    s1=abs(n-d1)
    s2=abs(n-d2)
else:
    d1=s[-1]
    d2=s[-3]
    s1=abs(n-d1)
    s2=abs(n-d2)
if s1==s2:
    print(d2,d1)
elif s1<s2:
    print(d1)
else:
    print(d2)
