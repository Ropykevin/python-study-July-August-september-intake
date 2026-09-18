# Create a new python file stringtask.py and attempt the 5 questions below:
# Clean up the following variable to give the clean version in lower case. Using inbuilt methods in the str class 
# name = “  JOHn  .“ to “john”

name ="   JOHn  ."
name=name.lower()
name=name.replace('.','')
name=name.strip()

print(name)

# Slice the below string to get you the resulting sentence:
# sentence_one = “The Dog Breed is German Shepherd” only display “Breed is German”

sentence_one = "The Dog Breed is German Shepherd"
print(sentence_one[8:23])

# sentence_two = “Defeats for the Clinton forces, this was her moment of triumph” only display “Clinton forces”

sentence_two = "Defeats for the Clinton forces, this was her moment of triumph"

print(sentence_two.index("s",24))
print(sentence_two[16:30])

# Split the below sentence using a semicolon i.e ; And display length of the result. 
# “The lazy dog; ran so fast; it hit the wall.” 
sentence3 = "The lazy dog; ran so fast; it hit the wall."

sentence3=sentence3.split(';')
print(sentence3)
print(len(sentence3))


# first_name="  Joh.n"  last_name="   Do,e" Clean up and display Full name i.e John Doe

first_name="  Joh.n"
last_name="   Do,e"

first_name=first_name.replace('.','')
first_name=first_name.strip()

last_name=last_name.replace(',','')
last_name=last_name.strip()

full_name=first_name+" "+last_name
print(full_name)

# Having the string r = '["E","W","C"]' #Manipulate it to display EWC

r = '["E","W","C"]'
r=r.replace(',','')
r=r.replace('"','')
r=r.replace('[','')
r=r.replace(']','')

print(r)
# Attempt questions in the link below. Whether you get the right answer or not, still read the solution explanation.
# https://realpython.com/quizzes/python-strings/
