# Question 1:

# A cinema charges:
# * ₹150 for ages under 18
# * ₹250 for ages 18–60
# * ₹100 for ages above 60

# Write a program that asks for age and prints the ticket price.

# age=int(input("Enter the age :"))
# if age < 18 :
#     print(150)
# elif age <= 60:
#     print(250) 
# elif age >60:
#     print(100)

# Question 2:

# A stadium sells entry passes with the following rules:
# * If age < 12 → Ticket = ₹50
# * If age between 12–59 → Ticket = ₹120
# * If age ≥ 60 → Ticket = ₹80


# Additionally, if the person’s age is a Even number, give a ₹5 discount.
# Get the input from the user and return the final discounted stadium ticket price.

        
age = int(input("Enter the age: "))

if age < 12:
    price = 50
elif age <= 59:
    price = 120
elif age >= 60:
    price = 80
if age % 2 == 0:
    price = price - 5  

print("Ticket Fare =", price)
