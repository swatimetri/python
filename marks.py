marks1 = int(input("enter the marsks1 "))
marks2 = int(input("enter the marsks2 "))
marks3 = int(input("enter the marsks3 "))
if(marks1<marks2 and marks1<marks3):
    res=(marks2+marks3)/2
elif(marks2<marks1 and marks2<marks3):
    res=(marks1+marks3)/2
elif(marks3<marks1 and marks3<marks2):
    res=(marks1+marks2)/2
print("average of two marks if {0}".format(res))
