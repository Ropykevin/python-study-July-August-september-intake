fruits = ['Mango', 'Oranges', 'Bananas', 'Lemon', 'Grapes']
print(fruits)
print(type(fruits))

# indexing and slicing
print(fruits[2])
print(fruits[-2])

# slicing used to extract a part of a list using index [start_index:end_index+1]
print(fruits[1:4])

# updating items in the list
fruits[1]='Tomatoes'

# append
fruits.append("Strawberries")
fruits.append('apple')
# insert
fruits.insert(3,'Watermelon')
# remove
fruits.remove('Lemon')
# pop
fruits.pop(2)
# clear =>Removes all the items in the list
fruits.clear()
print(fruits)

# create a list of days of the week
days=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
# display day today
print(days[1])
# display wednesday to saturday
print(days[3:7])
# update thursday to thur
days[4]='Thur'
# add january at the end of the list
days.append('January')
# add December between wednesday and thursday
days.insert(4, 'December')
# delete friday from the list
days.remove("Friday")
# delete the first item from the list
days.pop(0)
# delete the last item from the list
days.pop()
# delete all the items from the list
days.clear()
print(days)