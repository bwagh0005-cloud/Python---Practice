# write the double space from the  problem 3 with single space   
name = "WAGH  is good boy and "
print(name.find("  "))  # this will give the index of the first occurence of the double space in the string"))

print(name.replace("  "," "))  # this will replace the double space with single space in the string

print(name)   #''' this will give the original string with double space because the replace function does 
              # not change the original string it returns a new string with the replaced value '''
   #this is imutable property of the string in python that is we cannot change the original string 
 # but we can create a new string with the replaced value and assign it to the original variable name to change the original string