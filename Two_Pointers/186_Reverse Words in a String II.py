#Question
#Given an input string , reverse the string word by word.


#Two pointers solution

s=["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
s.reverse()

l,r=0,0

while l<len(s):
    space=l+1
    while str(s)!=' 'and space<len(s):
        space+=1
    r=space-1
    while r>l:
        s[l],s[r]=s[r],s[l]
        l+=1
        r-=1
    l=space+1
print(s)
    
