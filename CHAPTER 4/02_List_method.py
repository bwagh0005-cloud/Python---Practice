friends = ["sonu","monu","chintu","pintu"]
print(friends)
friends.append("RIDDHI")
print(friends)


# reverse() method is used to reverse the order of the list
l2 = ["sita","geeta ","namita","rahul"]
l2.reverse()
print(l2)




# append() method is used to add an element at the end of the list
l3 = ["145","652","759","1025+",]
l3.append("python")
print(l3)

# insert() method is used to add an element at a specific index in the list
l4 = ["MIT","HARWARD","STANFORD","UNIVERSITY OF COLUMBIAN ","OXFORD"]
l4.insert(4,"CAMBRIDGE")
print(l4) 

# pop() method is used to remove an element from a specific index in the list
# fulluy similar to the remoove but the difference is that the pop() method removes an element from a specific index in the list
#  and returns the removed element
# it's also used to remove the last element from the list if no index is specified


l5 = ["UNTOUCHABLE"," BUDDHAB AND DHAMMA","UNHILATION OF CAST","CAL MARSH"]
l5.pop(2)
print(l5)

# concatenation of two lists
l6 = [1,2,3]
l7 = [50,60,70]
print(l6+l7) #this will combine the two lists
print(l7+l6)

# repetition of lists
 
l8 = ["A","B","C"]
l9 = l8*3
print(l9) #this will repeat the list three times

l10 = ["A","B","C"]
l11 = ["D","E","F"]
print(l10*4) #this will repeat the list four times
print(l11*3) #this will repeat the list three times

# extending a list using extend() method
villan = ["ravan","kans","indrajeet"]
villan.extend(["mahadev","vishnu"])
print(villan)
print(len(villan)) #this will print the length of the list after extending it


# but what happen we just apply the append() method to add a list to another list
villan.append(["mahadev","vishnu"])
print(villan) #this will add the list as a single element to the list
print(len(villan)) #this will print the length of the list after appending it


# removing an element from the list using remove() method
fruits= ["apple","banana","orange","grape"]
fruits.remove("banana")
print(fruits)

# but what happen if we try to remove an element which is not present in the list
# fruits.remove("kiwi")      #this will raise a ValueError because "kiwi" is not present in the list
                        # so its give the error message "ValueError: list.remove(x): x not in list"

# but on the other hand similarly the 2 element is present then it's remove thr 1st  one
fruits= ["apple","banana","orange","grape","banana"]
fruits.remove("banana")
print(fruits) #this will remove the first occurrence of "banana" from the list



# COUNT() method is used to count the number of occurrences of an element in the list
fruits= ["apple","banana","orange","grape","banana"]
print(fruits.count("banana")) #this will return 2 because "banana" is present 2 times in the list
print(f"Number of occurrences of 'banana': {fruits.count('banana')}") #this will return 2 because "banana" is present 2 times in the list


numbers = [1,2,3,4,6,2,3,8,9,10]
print(f" the list is {numbers}")
item_to_count = int(input("Enter the number to count its occurrences in the list: "))
c= numbers.count(item_to_count)
print(f"Number of occurrences of '{item_to_count}': {c}") #this will return the number of occurrences of the input number in the list


# when we can't check manual so the above progra are used to check the number of occurrences of an element in the list

# IN operator is used to check if an element is present in the list or not

fruits= ["apple","banana","orange","grape"]
print ("banana" in fruits ) #this will return True because banana is present in the list
print("kiwi" not in fruits) #this will return True because "kiwi" is not present in the list
