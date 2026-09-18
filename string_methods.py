my_name="TechCamp KENYA"
# capitalize ->make the first character have upper case and the rest lower case.
print(my_name.capitalize())

# .lower(converts the string characters to lowercase) an .upper(converts string characters to uppercase)

text1="MY name IS KeVIn"
print(text1)
text2=text1.lower()
print(text2)
text3=text1.upper()
print(text3)

# strip ->used to remove leading and trailing spaces 

text4="      i am a student     "
print(len(text4))
print(text4)
text5=text4.strip()
print(text5)
print(len(text5))

#  clean sentence1 to "Python programming"
sentence1="    PYThon ProgrammING"

print(sentence1)
# clean sentence2 to "SOFTWARE DEVELOPMENT"
sentence2="Software DEVELOPMENT     "
# Clean sentence3 to "computer science"
sentence3="   COMputer ScieNCE   "


# replace ->used to replace a character in a string

sentence4="i am a python Developer"

sentence4=sentence4.replace('python','Java')

print(sentence4)

# count->used to count the appearance of a character in a string
sentence4 = "i am a python Developer"
print(sentence4.count('e'))

# split ->used to split a string using a character in the string
sentence4 = "i am a python Developer"
sentence5=sentence4.split('p')
print(sentence5)

# change sentence6 to Alex Mwangi
sentence6="Alex Kimani"

# count the number of times o has appeared in sentence7
sentence7="Python programming"

# Split sentence 8 using the colon
sentence8="Alex:Brian:mike:kevin"