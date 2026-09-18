my_name="TechCAMp KENYA"

# capitalize->
my_name.capitalize()
print(my_name)
my_name1=my_name.capitalize()
print(my_name1)

# upper
my_name2=my_name.upper()
print(my_name2)
# lower
my_name3=my_name.lower()
print(my_name3)
# title
my_name4=my_name.title()
print(my_name4)

# strip ->removes leading and trailing spaces

text="     I am a student learning Python     "
print(len(text))
print(text)

text1=text.strip()
print(len(text1))
print(text1)


# clean sentence1 to "Python programming"
sentence1 = "    PYThon ProgrammING"
sentence1=sentence1.strip()
sentence1=sentence1.capitalize()
print(sentence1)
# clean sentence2 to "SOFTWARE DEVELOPMENT"
sentence2 = "Software DEVELOPMENT     "
sentence2=sentence2.strip()
sentence2=sentence2.upper()
print(sentence2)
# Clean sentence3 to "computer science"
sentence3 = "   COMputer ScieNCE   "
sentence3=sentence3.lower()
sentence3=sentence3.strip()
print(sentence3)
# Clean sentence4 to "Techcamp Kenya"
sentence4="TECHcamp Kenya      "
sentence4=sentence4.strip()
sentence4=sentence4.title()
print(sentence4)

# replace

sentence5 = "I am a Python Developer"

sentence6 = sentence5.replace("Python",'Java')
print(sentence6)

# count
print(sentence5.count('e'))

# split
sentence7=sentence5.split()
print(sentence7)

# index
# print(sentence5.index('u'))

# find
print(sentence5.find('u'))


# change sentence6 to Alex Mwangi
sentence6 = "Alex Kimani"

# count the number of times o has appeared in sentence7
sentence7 = "Python programming"

# Split sentence 8 using the colon
sentence8 = "Alex:Brian:mike:kevin"