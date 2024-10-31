import math

while True:
    a = input()
    if(a[0] == '0'):
        break
    k,s = a.split()
    k = int(k)
    p = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
    t = ''
    if(k > 0 and k < 28):
        for i in range(len(s)):
            t = t + p[(p.index(s[i]) +k)%28]
        print(''.join(reversed(t)))
