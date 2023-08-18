str1=input("enter string one ")
str2=input("enter string two ")
cnt=1
if len(str2)< len(str2):
    short = len(str2)
    long = len(str1)
else:
    short = len(str1)
    long = len(str2)
for i in range (short):
    if str1[i]==str2[i]:
        cnt+=1
print("similarly b/w 2 string \n")
print(cnt/long)
