# Write a python program to calculate the square of a number entered by the user
a = int(input("Enter a number: "))
print("The square of the number is: ", a ** 2)         # this is the exponentiation operator in python
print("The square of the number is: ", pow(a, 2))    # this is the built in function to calculate the power of a number
print("The square of the number is: ", a * a)         # this is the multiplication operator to calculate the square of a number
# but what we can't write is a ^ 2 because ^ is a bitwise operator not an exponentiation operator in python