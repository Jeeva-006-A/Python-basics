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
# grades = {
#     "Aarav": 86,
#     "Meena": 91,
#     "Jeeva": 78
# }
# grades["Abi"]=95
# grades["Nathiya"]=98
# print(grades)
# grades["Jeeva"]+=21
# print(grades)

# top_src = max(grades.values())
# for i in grades:
#     if grades[i] == top_src:
#         print(f"Name:{i},Mark:{grades[i]}")




#Defining the baseclass
# class AppointmentList:
#     def __init__(self):
#         self.appointments = []


# class AppointmentBooking(AppointmentList):
#     def __init__(self):
#         super().__init__()
#         self.counter = 0
        
        
#     def book_appointment(self, patient, doctor, time):
#         #{"id": int, "patient": str, 
#         #"doctor": str, "time": str, "status": str}
#         self.counter = self.counter + 1
#         appointment = {}
#         appointment["id"] = self.counter
#         appointment["patient"] = patient
#         appointment["doctor"] = doctor
#         appointment["time"] = time
#         appointment["status"] = "BOOKED"
#         self.appointments.append(appointment)
        
#     def view_all_appointments(self):
#         print(self.appointments)

# ap_booking = AppointmentBooking()
# ap_booking.book_appointment("Ravi", "Mary", "1030 HRS")
# ap_booking.book_appointment("Yalini", "Priya","1830 HRS")
# ap_booking.view_all_appointments()


# class Rectangle():
#     def __init__(self,length,breath):
#         self.length = length
#         self.breath = breath
#     def Calculate_area_of_rectangle(self):
#         area = self.length*self.breath
#         return area
    
#     rect_area=10,20

#     print()

# class Circle:
#     def __init__(self,radius):
#         self.radius = radius

#     def calculate_area(self):
#         area=3.14*self.radius*self.radius
#         return area
# cir=Circle(10)  
# print(cir.calculate_area())

# class Student:
#     def __init__(self,name,age,mat,phy,che):
#         self.name=name
#         self.age=age
#         self.mat=mat
#         self.phy=phy
#         self.che=che
#         self.total_mark=0
#     def calculate_mark(self):
#         self.total_mark=self.mat+self.phy+self.che
#         return self.total_mark
#     def calculate_Grade(self):
#         if self.total_mark == 300:
#             return "S"
#         elif self.total_mark <= 250 and self.total_mark >= 300:
#             return "A Grade"
#         else:
#             return "Fail" 
# ans=Student("Jeeva",19,99,99,99)
# print(ans.calculate_mark())
# print(ans.calculate_Grade())                  

# class Product:
#     def __init__(self,id,name,qty,desc):
#         self.id=id
#         self.name=name
#         self.qty=qty
#         self.desc=desc
# class Cart:
#     def __init__(self):
#         self.Product_list=[]


#Write your code here
# class User:
#     def __init__(self,username,password,login_status,active):
#         self.username=username
#         self.password=password
#         self.login_status=login_status
#         self.active=active
#     def login_user(self):
#             if self.username == username and self.password ==password and active==True:
#                 return  "Login successful"
#             elif self.username == username and self.password ==password and active == False:
#                 return "User Inactive"
#             else:
#                 return "Invalid credentials"
#     def logout_user(self):
#         if login_status == True:
#             set= False
#             return "User logged out"
#         else:
#             return "User not found/already logged out"
            
#     def deactive_user(self):
#         if username == username:
#             active = False
#             return "User deactivated"
#         else:
#             return "User not found"
            
# user='jeeva','1234','False','True'

class User:
    def __init__(self):
        self.current_user = {}
    def add_user(self,username,password):
        self.current_user["username"]=username
        self.current_user["password"]=password
        self.current_user["login_status"]=False
        



        



