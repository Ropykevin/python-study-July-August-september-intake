# create a new file tuples_task.py
# 1. numbers = (10, 20, 30, 40, 50)Add 60 to the end,Replace 30 with 35.
numbers = (10, 20, 30, 40, 50)
# convert to list
numbers=list(numbers)
# modify
numbers.append(60)
numbers[2]=35
# convert back to tuple
numbers=tuple(numbers)
print(numbers)

# 2. values = (15, 5, 30, 25, 10) arrange the elements in ascending order.
values = (15, 5, 30, 25, 10)
# # convert to list
values=list(values)
# modify
values.sort()
# # convert back to tuple
values=tuple(values)
print(values)
# 3. fruits = ("apple", "banana", "cherry", "banana", "mango", "banana")
# Count occurrences of "banana",Remove all occurrences of "banana".
fruits = ("apple", "banana", "cherry", "banana", "mango", "banana")
print(fruits.count('banana'))

# # convert to list
fruits=list(fruits)
# modify
fruits.remove('banana')
fruits.remove('banana')
fruits.remove('banana')
# convert to tuple
fruits=tuple(fruits)
print(fruits)
# 4. names = ("Alice", "Bob", "Charlie", "David") Reverse the order of elements using sort method.
names = ("Alice", "Bob", "Charlie", "David")
# # convert to list
names=list(names)
# modify
names.sort(reverse=True)
# convert to tuple
names=tuple(names)
print(names)

# 5. colors = ("red", "blue", "green") add "yellow" at index 1,Extend with ["purple", "orange"]
colors = ("red", "blue", "green")
x = ["purple", "orange"]
# # convert to list
colors=list(colors)
colors.insert(1,'yellow')
colors.extend(x)
colors=tuple(colors)
print(colors)
# Attempt questions in the link below. Whether you get the right answer or not, still read the solution explanation.
# https://realpython.com/quizzes/python-lists-tuples/viewer/
