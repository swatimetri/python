n=int(input("enter the number"))
num=n
rev=0
num2= str(n)
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10

if(num==rev):
    print("yes")
else:
    print("no")
    
def palcount(n1):
    while(n1>0):
        dig=n1%10
        print(dig,"no of occurances",num2.count(str(dig)))
        n1=n1//10
        

palcount(num)
