
# Create a file called mydstask.py and attempt the below questions:
# my_ds = [23, “Jane”, (560), [“Lesson”, “Maths”, {“currency” : “KES”}], 987, (76,”John”)]
my_ds = [23, "Jane", (560), ["Lesson", "Maths", {"currency" : "KES"}], 987, (76,'John')]
print(type(my_ds))
# 1. Print KES
print(my_ds[3][2]["currency"])
# 2. Print 560
print(my_ds[2])
# 3. Print Maths
print(my_ds[3][1])
# 4. In the dictionary with the key currency, add another key “amount” with value 90 
print(my_ds[3][2])
my_ds[3][2]['amount']=90
my_ds[3][2]['currency']="USD"
print(my_ds)

# 5. Reverse 987 to 789 without using an inbuilt -method or Assigning 789 manually.
#      Hint: Strings can be reversed using [::]
# locate 987
print(my_ds[4])
# convert to an str
my_ds[4]=str(my_ds[4])
# reverse
my_ds[4]=my_ds[4][::-1]
# convert to an int
my_ds[4]=int(my_ds[4])

print(my_ds)
# 6. Change the name “John” to “Jane” .
# locate john
print(my_ds[5][1])
my_ds[5]=list(my_ds[5])
my_ds[5][1] = "Jane"
my_ds[5] = tuple(my_ds[5])
print(my_ds)
# You can research or discuss to find the solutions above.
#         https://realpython.com/quizzes/pybasics-tuples-lists-dicts/ 

# student1 = {
#     'name': "alex",
#     'age': 20,
#     'adm': "tech2015",
#     'city': 'Nairobi',
# }

# print(student1["age"])


# x = ["Lesson", "Maths", {"currency": "KES"}]
# x[0]

# my_name="Ropy"
# print(my_name[::-1])
# print(my_name[start:end+1:step])