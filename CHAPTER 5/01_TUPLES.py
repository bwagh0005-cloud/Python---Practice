# # tuples are immutables we can't change it ..
# # the tuples are the writen in round braket..
# # which can be separated by the comma

t1 = ("string", 1,1.5,True,None,[1,2,3],(10,20))
print(t1)
print(len(t1)) 

# # accesing the item element  = index

print(t1[0])
print(t1[-1])


# # without round bracket
t2 = 10,20,30,40
print(t1)
print(type(t1))


l1 =[10,20,30]
print(l1)
print(type(l1))
print(l1,type(l1))

t1 = tuple(l1)
print(t1)
print(type(t1))
print(l1,type(t1))
print(l1,type(l1))


# so now the converted tuples into the list

fruits = ("MANGO","BANANA","APPLE","ORANGES")
print(fruits,type(fruits))

# but now convert into list so 
fruits = list(fruits)
print(fruits,type(fruits))
# done