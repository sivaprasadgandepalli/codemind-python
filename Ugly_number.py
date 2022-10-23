def isugly(num):
        if num == 0:
            return False
        for i in [2, 3, 5]:
            while num % i == 0:
                num =num// i
        if(num==1):
            return True
        else:
            return False
n=int(input())
if(isugly(n)):
    print("Ugly Number")
else:
    print("Not Ugly Number")