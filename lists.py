fruits=['mango','oranges','apple','lemon','grapes']

print(fruits)
print(type(fruits))
# indexing and slicing
print(fruits[2])
print(fruits[-2])

# slicing->extracting a part of a list
# [start_index:end_index+1]
print(fruits[1:4])
print(fruits[2:5])

# updating items
fruits[2]='banana'
print(fruits)
# append
fruits.append('strawberries')
fruits.append('Watermelon')
# insert
fruits.insert(1,"Tomatoes")
print(fruits)

fruits.remove('oranges')
fruits.pop(0)
fruits.clear()
print(fruits)
# create a list of days of the week
days = ['monday', 'tuesday', 'wednesday',
        'thursday', 'friday', 'saturday', 'sunday']
# display the day today 
print(days[0])
print(days[-2])
# display tuesday to friday
print(days[1:5])

# update thursday to thur
days[3]='thur'
# add january at the end of the list
days.append('January')
# add december between tuesday and wednesday
days.insert(2,"December")
print(days)
# delete friday from the list
# delete the last item on the list
# delete the item at index 1
# delete all items from the list