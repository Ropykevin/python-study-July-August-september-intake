# Conditional Statements=>To make decisions based on a result of a certain Condition
# coditions are created using comparison operators(<,>,==,<=,>=,!=)
# conditions returns Booleans# 
# =>Python uses three primary Keywords on conditional statements(if,else,elif)

        # if Statements
# Executes a block of code only when the condition is true
            #syntax 
    # if condition:
            #block of code 
if 20>100:
    print('twenty is greater')
else:
    print('twenty is less')
age=40

if age>18:
    print('Adult')
else:
    print("Minor")
# auth users with age from 18 to 60
if age>=18 and age<=60:
    print('Allow Access')
else:
    print('Access Denied')

# check if the temperature is above 30 print too hot
# if else statement
# =>Else Executes the else block when the condition is false
        # Syntax
    #if condition:
            #if block
    #else:
            #else block

# print pass if student marks is above 50 otherwise fail
marks = 60

if marks >50:
    print('PASS')
else:
    print('Fail')


# if-elif-else =>to check multiple conditions with diff outcomes
# print pass if student marks is above 70,print Average if marks is 50 to 70 otherwise fail

if marks>70:
    print('Pass')
elif marks>=50 and marks<=70:
    print('Average')
else:
    print('Fail')
    
# print Senior Adult if age is above 50,print adult if age is above 20,print teenager if the age is above 12 otherwise print child

age =1

if age>50:
    print('Senior Adult')
elif age>20:
    print('Adult')
elif age>12:
    print('Teenager')
else:
    print("Child")
    
# print A if marks is above 80
# print B if marks is above 70
# print C if marks is above 60
# print D if marks is above 50
# otherwise print E

marks=0

if marks>80:
    print('A')
elif marks>70:
    print('B')
elif marks>60:
    print('C')
elif marks>50:
    print('D')
else:
    print('E')

# task
# slide 56 1 to 4
# slide 58 
# slide 59 3 and 4
            # nested if
