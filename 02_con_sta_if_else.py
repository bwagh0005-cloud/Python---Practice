# if -else

# if condition:
#     statement1   if the satement is "true" then execute the
# else:
#     statement2   if the satement is "false" then execute the

age = float((input ("what is your age:")))
if age >= 18:
    print("eligible for voting") 
else:
    print("it's not eligible for voting")
print("rest of the life")

# print if the number is even or odd
# odd - the number is the number which is not divisible by 2 & remainder is 1
# even - the number is the number which is divisible by 2 & remainder is 0


num = int(input("enter a number: "))
if num % 5== 0:
    print("this is an even number")
else:
    print("this is an odd number")

# # to print the number is positive or negative or zero


num = int(input("enter the integer number: "))
if num > 0:
    print("number is positive")
else:
    print("number is negative")


