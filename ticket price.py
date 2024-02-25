age = int(input("enter your age : \n"))
day = input("enter the day:\n")
# if age >= 18  and day == "wednesday":
#     print("the price is : 10$")
# elif age < 18 and day == "wednesday":
#     print("the price is 6$")
# elif age >= 18  and day != "wednesday":
#     print("the price is : 12$")
# elif age < 18 and day != "wednesday":
#     print("the price is 8$")
price = 12 if age >= 18 else 8

if day == "wednesday":
    price = price -2

print(price)
