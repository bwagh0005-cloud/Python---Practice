# membership operator{in , no in we use}
nums = {1,3,0,40,14,-1}
print(-1 in nums)
print(40 not in nums )
print(10 not in nums)

#  concatination
# nums_1 = {14,10,20,50}
# nums_2 = {7,4,10,50}
# print= {nums_1 + nums_2}
# so what we can say concatination not in set

# and also can't the make repetion

# repeating

# nums_1 = {1,2,3,4,5,6}
# print(nums_1*3)
# and also can't support the repetating element


# NOW CONVERTED THE TUPLE INTO SETS

weekdays = ("mon","tue","wed","thu","fri","sat")
weekdays = set (weekdays)
print(weekdays)


# add 
set_1 = {2,4,6}
print(set_1)
set_1.add(5)
print(set_1)

# remove
set_1 = {2,4,6}
print(set_1)
set_1.remove(6)
print(set_1)
# remove()   give the error of the element/item not set

# discard
set_1 = {2,4,6}
print(set_1)
set_1.discard(5) #so that's the difference in this ,if the element can't present in the set then it's  can't give the error
print(set_1)
# discard()  not give the error of the element/item not set
