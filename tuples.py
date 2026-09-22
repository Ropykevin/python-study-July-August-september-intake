        # Tuples
# =just like list they multiple items that can be of diff data type
# =items are ordered
# =>items are enclosed with ()
# =>Items are immutable(cannot be changed or modified)
# =>all tuples belong to class tuple
fruits = ('Mango', 'Oranges', 'Bananas', 'Lemon', 'Grapes')
print(type(fruits))
print(fruits[2])
print(fruits[1:4])
# convert to a list using list()
fruits=list(fruits)
print(type(fruits))
print(fruits)
# modify
fruits[2]="strawberries"
fruits.append('Watermelon')
print(fruits)

# convert back to a tuple using the tuple()
fruits=tuple(fruits)
print(type(fruits))
print(fruits)
days = ("monday", "tuesday", "wednesday",
        "thursday", "friday", "saturday", "sunday")
# 1. Find wednesday using an index
# 2. Using a function  find the length of the tuple.
# 3. Replace Thursday with Thur
