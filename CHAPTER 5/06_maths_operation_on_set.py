# the mathematical opertion like that the union , intersection, differance are like that


# intersection -
student_1 = {"math","english","scince","cs","physics","chemistry","finance"}
student_2 = {"math","english","scince","cs","chemistry","sanskrit"}

student_3 = student_1 & student_2  #ampersand we call the symbol"&"
# also the second method to write this
student_4 = student_1.intersection (student_2)
print(student_3)

# union -
student_5 = student_1.union(student_2)
print(student_5)
# also the second method to write this
student_5 = student_1 | student_2 #| sympol call pipe
print(student_5)


# differance -
student_6= student_1.difference(student_2)
print(student_6)

# also the second method to write this

# the element not in the 1st one but present in second one visivesa which are in the 2nd but not in the 1st
#  represented by *-*
weekdays ={"mon","tue","wed","thu","fri","sat"}
days = {"sun","mon"}
weekdays = days - weekdays
print(weekdays)
weekdays = weekdays - days #set() is 
print(weekdays)

# when we can't get comman in more than the 2 more set it's should be the "empty sets"
