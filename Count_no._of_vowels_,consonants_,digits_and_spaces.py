s=input()
vowels="aeiou"
v=0
c=0
d=0
sp=0
for i in range(0,len(s)):
    if(s[i].isdigit()):
        d+=1
    elif(s[i].isspace()):
        sp+=1
    elif(s[i].isalpha()):
        if s[i] in vowels:
            v+=1
        else:
            c+=1
print("Vowels: "+str(v))
print("Consonants: "+str(c))
print("Digits: "+str(d))
print("White spaces: "+str(sp))
            
        
