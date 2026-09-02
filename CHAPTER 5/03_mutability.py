# mutability &  immutability
# list are mutables
# tuples amd String are immutables


# String
s1 = "python is language"
print(s1)
# now simply we do one thing we just replace it
s1.replace("python","java")
print(s1)
# but we can see the output can't so we now so make new string 
s2 = s1.replace("python","java")
print(s2)


#Tuples
t1 = ("mango","orange","banana","watermelon")
print(id(t1)) 

# list
t2 = ["mango","orange","banana","watermelon"]
t2[-1] = "apple"
print(t2)
print(id(t2))

