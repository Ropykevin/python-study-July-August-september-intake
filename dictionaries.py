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
}
print(student1['country'])
# add and update properties
student1['city']='Nairobi'
print(student1)
# add County Kisumu
# update
student1['age']=30
print(student1)
# update name