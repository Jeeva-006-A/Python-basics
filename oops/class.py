# class Vehicle:
#     def __init__(self, wheels, fuel_type, speed, price):
#         self.wheels = wheels
#         self.fuel_type = fuel_type
#         self.speed = speed
#         self.price = price
#     def show_details(self):
#         print(f"Number of wheels: {self.wheels}")
#         print(f"Price of the vehicle: {self.price}")
#         print(f"Speed of the vehicle: {self.speed}")
#     def accelerate(self):
#         self.speed += 10
# class Car(Vehicle):
#     def __init__(self, wheels, fuel_type, speed, price):
#         super().__init__(wheels, fuel_type, speed, price)
# new_car = Car(wheels=4, fuel_type="petrol", speed=60, price=100000)
# new_car.show_details()
# new_car.accelerate()
# new_car.show_details()
# print("Accelerating the car again")
# new_car.accelerate()
# new_car.show_details()


word="newspaper"
letter=word[0]
for i in range(len(word)):
    if word [i]<letter:
        letter=word[i]
print(letter)