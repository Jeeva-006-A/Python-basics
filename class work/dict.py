# stud_dict = {"Antonia": 90,
#         "Jeeva":60,
#         "Amstrong": 51,
#         "Ragavi": 81,
#         "Preethi": 75 }

# print(stud_dict)
# query = "Antonia"
# print(stud_dict[query])
# stud_dict["Antony"] = 10
# print(stud_dict)
# query = "Antony"
# print(stud_dict[query])

# super_hero_dict = dict()
# names = ["John", "Banner", "Mark", "Krish","Tony","Natasha"]
# power_level = [1000, 1000000, 700, 8000,3000, 1500 ]

# for i in range(len(names)):
#     super_hero_dict[names[i]] = power_level[i]

# print(super_hero_dict)

# super_hero_names = super_hero_dict.keys()
# super_hero_powervalues = super_hero_dict.values()
# print(list(super_hero_names))

# del super_hero_dict["Mark"]
# print(super_hero_dict)

# for key, value in super_hero_dict.items():
#     print(key, value)

# 1.Take two list names, marks and create a dictionary with name as key and value as marks
# 2.In the dictionary created. find the students who have scored more than PASS_MARK .
# 3.Ask the user to enter 3 user names as Ganesh,Suresh,Priyanka and their corresponding marks 50, 40,60 and add it to the dictionary

result=dict()
names=['Jeeva','Nathiya','Yashika','Kamalesh','Anto']
marks=[75,90,94,92,80]

for i in range(len(names)):
    result[names[i]]=marks[i]
print(result)

pass