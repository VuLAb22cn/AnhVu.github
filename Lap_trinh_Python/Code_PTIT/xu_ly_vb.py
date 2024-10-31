import re

def progress_s(s):
    s = re.sub(r'[.?!]','',s)
    s = s.strip()
    if s:
        s.lower().capitalize()
    return s

def progress_wrap(text):
    mang = re.split(r'[.?!]+',text)
    result = [progress_s(s) for s in mang if s.strip()]
    return result

text = input()
s = progress_wrap(text)
for i in s:
    print(s)

    