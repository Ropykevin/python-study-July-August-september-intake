# Conditional statements
# Used to make decisions Based on a result of a certain condition
# Conditions are created using comparison operators(==,<,>,!=,>=,<=)
#Conditions returns True or False 
# In python programming language we have 3 main key words for conditional statements(if,else and elif)

            # if statement
# =>executes/run a block of code when the condition is True
#               syntax
#if condition:
    #if block 
if 20>100:
    print('20 is greater')
else:
    print('20 is less')
    
age=10

if age>=18:
    print("Adult")
else:
    print("Minor")
    
# users are allowed to join the website only if the age is from 18 to 60
if age>=18 and age<=60:
    print('Access Granted')
else:
    print("Access Denied")
# check if temperature is above 30 print too hot 
temperature=40
if temperature>30:
    print('too hot')

marks=90
if marks>50:
    print('Pass')
    
#    if-else statement=>else executes the else block when the condition is false(otherwise of if)
        # syntax
    #if condition:
        # if block
    #else:
        # else 
        
# print access Granted if password is similar with Admin@254! otherwise access Denied

password=input("Enter your password:")
correct_password = 'Admin@254!'

if password==correct_password:
    print("access Granted")
else:
    print("Access Denied")
    
# if-elif-else=>Elif is used when we have multiple conditions with different outcomes 
# syntax
# if condition:
    # if block
# elif condition:
    # elif block1
# elif condition:
    # elif block2
# else:
    # else block
    
    # temperature
temperature=20
if temperature>30:
    print('Too hot')
elif temperature>15:
    print("normal temperature")
else:
    print("cold temperature")

    # age 
age=10

# senior adult above 50
# above 20 Adult
# above 12 Teenager
# otherwise a child

if age>50:
    print("Senior Adult")
elif age>20:
    print('Adult')
elif age>12:
    print("Teenager")
else:
    print("Child")
    
# print A if marks is above 80
# print B if marks is above 70
# print C if marks is above 60
# print D if marks is above 50
# otherwise print E

marks=120

if marks>=0 and marks<=100:
    if marks>80:
        print('A')
    elif marks>70:
        print("B")
    elif marks>60:
        print("C")
    elif marks>50:
        print("D")
    else:
        print("E")
else:
    print('Invalid Marks')


# task
# slide 56 1 to 4
# slide 58 1 and 2
# slide 59 3 and 4

        # nested if
