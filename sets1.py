#Sets
# =>Data structures that stores multiple items that can be of any type
# =>items in are set are unordered (no index)
# =>items in a set are unique
# =>enclosed with Curly brackets {}
# =>items are mutable
# class set

fruits = {'Mango', 'Mango', 'Mango',
          'Mango', 'Oranges', 'Bananas', 'Lemon', 'Grapes'}

print(fruits)
print(type(fruits))

# add
fruits.add('Strawberries')
print(fruits)

# remove or discard
fruits.remove('Bananas')
print(fruits)

days = {"monday", "tuesday", "wednesday", "thursday", "friday",
        "saturday", "sunday", "sunday", "sunday", "sunday"}
print(days)

# Remove friday and sunday from the set using methods.
# Add them back to the set
