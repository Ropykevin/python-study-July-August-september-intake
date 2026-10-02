# # Python Loops
# # Used to perfom repetitive tasks multiple times or until a certain condition is met

# # We have 3 loop commands in python
# # For loop
# # while loop

#         # For loop
# # =>used iterate over a sequence(strings,lists,tuples)
# # syntax
# # for iterator in sequence:
#     # block of code  
# # iterator->represents each character/item in the sequence
# # block of code repeated task
# fruits = ['mango', 'oranges', 'apple', 'lemon', 'grapes']
# for i in fruits:
#     print("Alex")

# numbers=[10,20,30,40,50]
# for num in numbers:
#     print('hello')
# # disply your name 10 times 
# nums=list(range(1,11))
# for i in nums:
#     print('Kevin')
# #display TechCamp 20 times
# my_list=list(range(1,21))

# for i in my_list:
#     print("TechCamp")
    
# # range(start end+1)->used to create  list of numbers 
# lst=list(range(1,201))
# print(lst)


# display even numbers btwn 1 and 100

lst1=list(range(1,101))
even=[]
for i in lst1:
    if i%2==0:
        even.append(i)

print(even)
# display numbers divisible by 5 from numbers between 100 and 150

lst2=list(range(100,151))
divisible=[]
for i in lst2:
    if i%5==0:
        divisible.append(i)
print(divisible)
        
# display odd numbers btwn 1 and 100
lst5=list(range(1,101))
odd=[]
for i in lst5:
    if i%2!=0:
        odd.append(i)

print(odd)
#  display numbers divisible by 3 and  5 from numbers between 100 and 200

lst6=list(range(100,201))
div=[]
for x in lst6:
    if x%3==0 and x%5==0:
        div.append(x)      
print(div)

# display in a list numbers disible by 5 and 7 from numbers btwn 1 and 100

lst7=list(range(1,101))

div5=[]
for i in lst7:
    if i%5==0 and i%7==0:
        div5.append(i) 
        
print(div5)

# break ->used to stop the loop
lst7 = list(range(1, 10))

for i in lst7:
    print('test')
    if i==2:
        break
    
# simcard pin
lst8=list(range(1,4))
attempts=3
for x in lst8:
    pin=input("Enter your pin:")
    correct_pin="1234"
    if pin==correct_pin:
        print("Access granted")
        break
    else:
        rem=attempts-x #calculating the number of rem attempts
        if rem==0:
            print("Account blocked")
        else:    
            print(f"Wrong pin try again you have {rem} attempts remaining")
