# Questions create a new file
# Convert a float to an integer with an inbuilt function in Python
# temp = 56.8926 to 57
temp = 56.8926
temp = round(temp)
print(temp)

# Convert the float below to give the results as follows
# temp = 56.8926 to 56.89
temp = 56.8926
temp=round(temp,2)
print(temp)

# Convert the float below to give the results as follows
# temp = 56.8926 to 56.893
temp = 56.8926
temp = round(temp, 3)
print(temp)
# Convert the float below to give the results as follows
# temp = 56.8926 to 8.926
# NB: Use string  slice & concatenation, but have result as float

temp = 56.8926
# convert to string
temp=str(temp)#"56.8926"
# slice 8926
temp = temp[3:]  #"8926"
# concat to include the dot
temp = temp[0]+'.'+temp[1:]
# convert back to a float
temp=float(temp)
print(temp)
print(type(temp))

# convert to 5.678
my_float = 5678.4567
# convert string

my_float=str(my_float)

# slice
my_float=my_float[0:4] #5678

my_float=my_float[0]+'.'+my_float[1:]


my_float=float(my_float)
print(my_float)



# convert to 456.7
my_float = 5678.4567


x="1000"
y="5000"

x=int(x)
y=int(y)
z=x+y
print(z)



# Attempt questions below. Whether you get the right answer or not , still read the solution explanation.
# https: // realpython.com/quizzes/python-data-types/
