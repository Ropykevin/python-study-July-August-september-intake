# Take three inputs from a user, separately. Print the largest of the numbers.
# Hint: Determine what type of data is taken in as input.

num1=input('Enter first number:')
num2=input("Enter second number:")
num3=input("Enter third number: ")

num1=int(num1)
num2=int(num2)
num3=int(num3)

if num1>num2 and num1>num3:
    value=(f'{num1} is the largest')
elif num2>num1 and num2>num3:
    value=(f'{num2} is the largest')
else:
    value=(f'{num3} is the largest')

print(value)
# name=input('Enter your name ')

# print(f"hello {name} how is you day today")


# 3.Write a Python program that checks if a variable x is between 10 and 20 (inclusive)
# and if another variable y is greater than 100. If both conditions are true, print "Conditions met", otherwise print "Conditions not met"
x=17
y=120

if x>=10 and x<=20 and y>100:
    res='Conditions met'
else:
    res="Conditions not met"

print(res)