# Create a class Temperature with one attribute celsius.
# Add two methods:
# class Temperature:
#     def __init__(self, celsius):
#         self.celsius = celsius 

#     def to_fahrenheit(self):
#         return (self.celsius * 9/5) + 32

#     def to_kelvin(self):
#         return self.celsius + 273.15
    
# temp = Temperature(25) 

# print("Celsius:", temp.celsius)
# print("Fahrenheit:", temp.to_fahrenheit())
# print("Kelvin:", temp.to_kelvin())


# c_name = ["Ravi Meena Ravi Kiran Meena Ravi Kiran"]
# rcount = 0
# mcount = 0
# kcount = 0
# words = c_name .split(" ")
# for i in words:
#     if i == "Ravi":
#         rcount +=1
#     elif i == "Meena":
#         mcount +=1
#     elif i == "Kiran":
#         kcount+= 1

# if rcount > mcount and 




# arr = "Mahendra Singh Dhoni"
# name= arr.split(" ")
# for i in name:
#     if name:
#         print(i[0],end="")

# if -98:
#     print("Its True")
# else:
#     print("Its False")

# users = {
#     "Jeeva":"Jeeva@2006",
#     "Antonia":"Anto@2008",
#     "Nathiya":"Nathiya@2007",
#     "Muthuselvi":"Muthu@2007"
# }

# def login_system(username,password):

#  if username in users:
#     if users[username] == password:
#         print("Login Successful")
#     else:
#        print("Invalid Password")
#  else:
#     print("User Not Found")


# login_system("Jeeva","Jeeva@2006")
# login_system("Nathiya","Nathiya@123")
# login_system("Muthu","Muthu@2007")




# inventory = {"apple": 10, "banana": 5, "mango": 8}

# inventory["apple"]+=4
# inventory["grape"]=6
# inventory["orange"]=7
# print(inventory)

# order = {
#   "burger": 120,
#   "fries": 70,
#   "juice": 60
# }


# total = sum(order.values())
# if total > 200:
#     total -= total * 0.10  
# print("Total Bill:",total)


# 4. Student Grades Record
# Store student marks in a dictionary:
# Write a function to:
# Add or update a student’s mark.
# Find and print the top scorer’s name and mark.
grades = {
    "Aarav": 86,
    "Meena": 91,
    "Jeeva": 78
}
grades["Abi"]=95
grades["Nathiya"]=98
print(grades)
grades["Jeeva"]+=21
print(grades)

top_src = max(grades.values())
for i in grades:
    if grades[i] == top_src:
        print(f"Name:{i},Mark:{grades[i]}")

