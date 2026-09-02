# concatination

student_detail1= (1001,"john")
student_detail2 =( 40,50,20,45,64)

# # # # + (means join the tuples together)
student_detail = student_detail1 + student_detail2
print(student_detail)

# # # # repetation
t1 = ("john",5000)
print(t1*3)
# we just use the * for the repetation of the element

# membership
# in this we just use the "IN" and "NOT" operation

print(40 in  student_detail2)
print(45 not in  student_detail2)
# it's just for the check


# count
# for the tuples.count(element)

t2= (10,20,30,40,10,50,100)
print(t2)
print(t2.count(10))

print(t2.count(41))


# Index 
# index syntax as same as the "count" 
# just like the tuples.index(element)
#  on the element we cann store the which vales on the tuples the y shhow the index of the element
# (element) 

t3= (22,33,44,55,66,77,88,99,100,45,55)
print(t3)
print(len(t3))
print(t3.index(44)) #Now simply the index of 44 in tuples t3 ?
print(t3.index(55)) #NOW THE TWIST IS THE THE 55 COME IN THE TUPLES 2 TIMES ON THE INDEX OF 3 AND 11, BUT WE JUST GAVE IT'S THE 1ST ONE
                    #  WHEN THE SIMILAR ELEMENT PRESENT IN THE TUPLES WE JUST GATE THE 1ST ELEMENT

                                                                                              
# Min
print(f"smallest number : {min(t3)}")

# max
print(f"biggest number: {max(t3)}")

# sum
print(f"sum of number :{sum(t3)}")
# or we can say total of number
print(f"total of number :{sum(t3)}")

