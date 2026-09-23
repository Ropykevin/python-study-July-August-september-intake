# create a new file tuples_task.py
# 1. numbers = (10, 20, 30, 40, 50)Add 60 to the end, Replace 30 with 35.

numbers = (10, 20, 30, 40, 50)
# convert to list
numbers = list(numbers)
# modify
numbers.append(60)
numbers[2]=35
# convert to tuple 
numbers=tuple(numbers)

print(numbers)
# 2. values = (15, 5, 30, 25, 10) arrange the elements in ascending order.
values = (15, 5, 30, 25, 10)

values=list(values)

values.sort()
values =tuple(values)
print(values)
# 3. fruits = ("apple", "banana", "cherry", "banana", "mango", "banana")
# Count occurrences of "banana", Remove all occurrences of "banana".
fruits = ("apple", "banana", "cherry", "banana", "mango", "banana")

print(fruits.count("banana"))

fruits=list(fruits)

fruits.remove("banana")
fruits.remove("banana")
fruits.remove("banana")
fruits=tuple(fruits)
print(fruits)
# 4. names = ("Alice", "Bob", "Charlie", "David") Reverse the order of elements using sort method.
names = ("Alice", "Bob", "Charlie", "David")

# convert to list
names=list(names)
# sort
names.sort(reverse=True)
# convert back to a tuble 
names=tuple(names)
print(names)
# 5. colors = ("red", "blue", "green")add "yellow" at index 1, Extend with ["purple", "orange"]
colors = ("red", "blue", "green")

colors=list(colors)
colors.insert(1,'Yellow')
x = ["purple", "orange"]
colors.extend(x)

colors=tuple(colors)
print(colors)
# Attempt questions in the link below. Whether you get the right answer or not, still read the solution explanation.
# https: // realpython.com/quizzes/python-lists-tuples/viewer/
