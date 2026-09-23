#          Dictionaries
# => Stores multiple properties in key-value pairs key:(value)
# =>enclosed with {curly braces}
# =>Keys are always strings but values can be of any type
# keys are unique
# class 'dict'

student1 = {
    'name': "alex",
    'age': 20, 
    'adm': "tech2015",
    'city':'Nairobi',
    }

print(student1)
print(type(student1))

# displaying values
print(student1['name'])
print(student1['city'])
# display adm

# adding and updating

# adding
student1['Gender']='Male'
print(student1)
# add a new key email with value

# updating
student1['age']=30
print(student1)
# update name with a diff name