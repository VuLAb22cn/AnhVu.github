def ucln(a,b):
    if(b == 0):
        return a;
    else:
        return ucln(b,a%b);

t = int(input())
while(t-- > 0):

