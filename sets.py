#       Sets
# Data structure that stores multiple items of different types
# items are mutable 
# items are unordered(no index)
# items are unique (no duplicate items )
# enlosed with {} curly brackets

fruits = {'mango', 'mango', 'mango','oranges', 'apple', 'lemon', 'grapes'}
print(fruits)

fruits.add('strawberries')
print(fruits)
# remove or discard
fruits.remove('grapes')
print(fruits)

days = {"monday", "tuesday", "wednesday", "thursday", "friday",
        "saturday", "sunday", "sunday", "sunday", "sunday"}
print(days)


# Remove friday and sunday from the set using methods.
# Add them back to the set
# set()->converts variables to sets