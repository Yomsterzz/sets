"""#converting a list to a set
sample_list = [56, 87, 56, 87]
sample_set = set(sample_list)
print(sample_set)

if 56 in sample_set:
    print("Yes, the number exists!")
else:
    print("No, the number does not exist.")

#adding elements to a set
myset = set([])
print(type(myset))
myset.add(77)
myset.add(57)
myset.add(27)
myset.add(25)
myset.add(22)
myset.add(73)
myset.add(71)
myset.add(71)
myset.add(73)
print(myset)

myset.remove(73) #gives error if doesn't exist
print(myset)

myset.discard(77) #doesn't give error if doesn't exist
print(myset)"""

#set operations
#union | intersection | difference | symmetric difference
a = {12, 34, 56, 78, 90, 9}
b = {98, 76, 54, 32, 78, 56, 21}

print(b.union(a))
print(b.intersection(a))
print(b.difference(a))
print(b.symmetric_difference(a))