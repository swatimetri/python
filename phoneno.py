import re
def isphonenumber(numstr):
    if len(numstr)!=12:
        return False
    for i in range (len(numstr)):
        if i==3 or i==7:
            if numstr[i]!="-":
                return False
        else:
                if numstr[i].isdigit()==False:
                     return False
    return True

def chkphnumber(numstr):
     phnopattern=re.compile(r'^x  \d{3}-\d{3}-\d{4}$')
     if phnopattern.match(numstr):
          return True
     else:
          return False
phnum=input("enter phone number : ")
print("without using regular expresson")
if isphonenumber(phnum):
    print("valid phone number")
else:
    print("invalid phone number")        
print("using regular expressioin")
if chkphnumber(phnum):
    print("valid phone number")
else:
    print("invalid phone number")           
