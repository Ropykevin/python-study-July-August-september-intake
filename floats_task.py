# Questions create a new file
# Convert a float to an integer with an inbuilt function in Python
# temp = 56.8926 to 57
temp = 56.8926
temp1=round(temp)
print(temp1)
# Convert the float below to give the results as follows
# temp = 56.8926 to 56.89 

temp = 56.8926
temp2=round(temp,2)
print(temp2)

# Convert the float below to give the results as follows
# temp = 56.8926 to 56.893 
temp = 56.8926

teamp3=round(temp,3)
print(teamp3)
# Convert the float below to give the results as follows
# temp=56.8926 to 8.926 
# NB: Use string  slice & concatenation, but have result as float 

temp = 56.8926
# convert to a string
# str()->converts variables into strings
temp=str(temp)#'56.8926'
# slice
temp = temp[3:]
# concat
temp = temp[0]+'.'+temp[1:] #8 + '.' + 926
print(temp)#8926
# float()->converts numeric variables to floats
temp=float(temp)
print(type(temp))


# convert to 5.678
my_float = 5678.4567

my_float = str(my_float)  # "5678.4567"
my_float=my_float[0:4]

print(my_float)  # 5678

my_float=my_float[0]+'.'+my_float[1:]

print(my_float)

my_float=float(my_float)
print(type(my_float))

# convert to 456.7
my_float = 5678.4567

my_float=str(my_float)

my_float=my_float[5:]#4567

my_float=my_float[0]+'.'+my_float[1:]

my_float=float(my_float)
print(my_float)


# int()=>converts numerict variables into integers

x='2000'
y='2000'

x=int(x)
y=int(y)

# str()
# float()
# int()

z=x+y
print(z)
# Attempt questions below. Whether you get the right answer or not, still read the solution explanation.
# https://realpython.com/quizzes/python-data-types/
