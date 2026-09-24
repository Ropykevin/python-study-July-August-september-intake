#            Dictionaries
# Data structure that stores multiple properties in key-value pairs (key:value)
# enclosed with {} curly brackets
# keys are always strings but the values can be of any type
# keys are always unique
# Have no index we use keys to access values
student1={
    "name":'Mike',
    "age":21,
    "country":"Kenya",
    "gender":'Male',
    "hobbies":['Painting','Writing','Hiking']
}
print(student1['country'])
print(student1.get('country'))
# add and update properties
student1['city']='Nairobi'
print(student1)
# add County Kisumu
# update
student1['age']=30
print(student1)
# update name
# add a new key skills with values ["Web dev","UI",UX]
student1['skills']=["Web dev","UI",'UX']
print(student1['skills'][1])
print(student1["hobbies"][2])

student1['hobbies'].remove('Hiking')
print(student1)

del(student1['gender'])
print(student1)

# keys
print(student1.keys())
# values
print(student1.values())
# items
print(student1.items())

#get
print(student1.get('age'))