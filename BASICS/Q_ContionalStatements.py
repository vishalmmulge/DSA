marks = int(input("Enter your marks: "))

if(marks >= 90):
    print("Your Grade is A")
elif(marks < 90 & marks >= 80):
    print("Your Grade is B")
elif(marks < 80 & marks >= 70):
    print("Your Grade is C")
elif(marks <= 70):
    print("Your Grade is D")