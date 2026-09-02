# l1 = (5,1.5,"python",True,None,[1,2,3],10)

# print(l1)
# print(len(l1))
# print(l1[-2])
# print(l1[-2][0]) #this is the part of he chaining or wecan say the chaining index
# innthe cbaining index we can access the list inside the tuple by using the index of the list inside the tuple


# now the list inside the list ...
# its called nested list...we can write "n "numbres" in the list inside the list and we can access the numbers by using the index of the list inside the list

l2=[[1,2,3],[4,5,6],[7,8,[9,10]]]
print(l2)
print(len(l2))
print(l2[-1][-1])   #here we are accessing the last list inside the last list 
print(l2[-1][-1][-1])
