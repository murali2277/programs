import re
text="My name is MK and my E-mail is 0904_murali@gmail.com 2244"
match=re.search(r'[a-zA-z]+',text)
print(match)
match=re.findall(r'[a-zA-z\-]+',text)
print(match)
match=re.findall(r'[0-9]+',text)
print(match)
match=re.findall(r'[0-9]',text) 
print(match)
match=re.findall(r'[0-9a-z\_]+@+[a-z]+\.[a-z]+',text)
print(match)
match=re.findall(r'\.\w\w\w',text)
print(match)