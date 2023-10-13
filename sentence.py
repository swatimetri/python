sentence=input("enter a sentence")
worlin=sentence.split(" ")
print("this sentenc has ",len(worlin)-1,"words")
dig=upcnt=locnt=0
for ch in sentence:
    if '0'<=ch <='9':
        dig+=1
    elif 'A'<=ch <='Z':
        upcnt+=1
    elif 'a'<=ch <='z':
        locnt +=1
print("the sentence has ",dig," digits ",upcnt," upper case litter ",locnt," lower case letters")
