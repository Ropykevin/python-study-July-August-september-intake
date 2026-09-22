#               Tuples 
# =>Just like lists tuples store multiple items that can be of any datatype
# =>items are ordered (hve index)
# =>items in a tuple are immutable(cannot be changed)
# =>items are enclosed with normal brackets () 
# =>all tuples belongs to class tuple

fruits = ('Mango', 'Oranges', 'Bananas', 'Lemon', 'Grapes')
print(fruits)
print(type(fruits))
# index
print(fruits[2])
# slicing
print(fruits[1:4])
# convert to list using list()
fruits=list(fruits)
print(fruits)
print(type(fruits))
# modify
fruits[2]="Strawberries"
print(fruits)
fruits.append('WaterMelon')
print(fruits)
# convert back to tuples using the tuple()
fruits=tuple(fruits)
print(fruits)
print(type(fruits))

days = ("monday", "tuesday", "wednesday",
        "thursday", "friday", "saturday", "sunday")
# 1. Find wednesday using an index
print(days[2])
# 2. Using a function a find the length of the tuple.
print(len(days))
# 3. Replace Thursday with Thur

days=list(days)
days[3]="Thur"
days=tuple(days)
print(days)