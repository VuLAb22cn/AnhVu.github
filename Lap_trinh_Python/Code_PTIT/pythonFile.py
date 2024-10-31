import math

s = input()
s = s.lower()
if(s[len(s)-3]=='.' and (s[len(s)-2]=='p'  ) and (s[len(s)-1]=='y')):
    print("yes")
else:
    print("no")

