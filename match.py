import re
phone=re.compile(r'\+\d{12}')
email=re.compile(r'[a-za-z0-9._]+@[z-za-z0-9]+\.[A-Z|a-z]{2,}')
with open('dhanush.txt','r')as f:
    for line in f:
        matches=phone.findall(line)
        for match in matches:
            print(match)
        matches=email.findall(line)
        for match in matches:
            print(match)
