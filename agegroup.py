age = int(input("enter your age : \n"))

if age < 13 :
    print("child")
elif age >= 13 and age <= 18:
    print("Teenager")
elif age >= 20 and age <= 59:
    print("Adult")
else:
    print("Senior")       