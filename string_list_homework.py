#qst1
list1=range(1,299)
list2 = [x for x in list1 if x % 2 == 0]
print(list2)
#qst2 
print("the size of my list is ",len(list2))
for x in list2:
    print("square of",x, "is",x**2)
#qst3
print(57 in list2)