#          Dictionaries
# => Stores multiple properties in key-value pairs (key:value)
# =>enclosed with {curly braces}
# =>Keys are always strings but values can be of any type
# =>keys are unique
# =>class 'dict'

student1 = {
    'name': "alex",
    'age': 20,
    'adm': "tech2015",
    'city': 'Nairobi',
    'skills': ['UI', 'UX', 'Web']
}

print(student1)
print(type(student1))

print(student1['skills'][1])

# print(student1.get('skills'))
# # displaying values
# print(student1['name'])
# print(student1['city'])
# # display adm
# print(student1['adm'])
# # adding and updating

# # adding
# student1['Gender']='Male'
# print(student1)
# # add a new key email with value

# # updating
# student1['age']=30
# print(student1)
# # update name with a diff name
# student1['name']='Mike'

# # Delete aproperty
# del(student1['age'])
# print(student1)

# # .get() displaying values
# print(student1.get('adm'))

# # .keys ->used to display a list of all keys
# print(student1.keys())
# # .values->used to display a list of all values
# print(student1.values())
# # items->list of tuples of each property
# print(student1.items())
