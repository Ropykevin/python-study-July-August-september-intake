# Python Loops
# Used to perfom repetitive tasks multiple times or until a certain condition is met

# We have 3 loop commands in python
# For loop
# while loop

        # For loop
# =>used iterate over a sequence(strings,lists,tuples)
# syntax
# for iterator in sequence:
    # block of code  
# iterator->represents each character/item in the sequence
# block of code repeated task
fruits = ['mango', 'oranges', 'apple', 'lemon', 'grapes']
for i in fruits:
    print("Alex")

numbers=[10,20,30,40,50]
for num in numbers:
    print('hello')
# disply your name 10 times 
nums=list(range(1,11))
for i in nums:
    print('Kevin')
#display TechCamp 20 times
my_list=list(range(1,21))

for i in my_list:
    print("TechCamp")
    
# range(start end+1)->used to create  list of numbers 
lst=list(range(1,201))
print(lst)