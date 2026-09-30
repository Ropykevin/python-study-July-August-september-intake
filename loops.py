#       Python Loops
# Used  to perfom a repetitive task multiple times or until a certain condition is met
# Python has two loop commands
# for loop
# while loop

#  for loop
# used to iterate over a sequence(strings,lists,tuples)
# syntax

# for iterator in sequence:
    # block of code
    
# iterator->a variable that represents each item in the sequence 
# block of code->repeated task 

fruits = ['mango', 'oranges', 'apple', 'lemon', 'grapes']
for fruit in fruits:
    print("i am a student")
    
numbers=[10,20,30,40,50]
for i in numbers:
    print(i)
    
nums=[100,200,300,400,900]
for i in nums:
    print('hello')
    
# display your name 10 times
my_list=list(range(1,11))
for i in my_list:
    print("Ropy")

# print Techcamp 100 times 
# range(start,stop+1) creates a sequence of numbers
numbers=list(range(1,101))

for i in numbers:
    print('TechCamp') 
