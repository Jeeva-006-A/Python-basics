# 1.SUM
#  Write a function to print all numbers from a to b using a loop.
# def print_numbers(a, b):
#     # write your code here
# print_numbers(1, 5)
# print_numbers(3, 8)
# print_numbers(10, 12)

# def print_numbers(a,b):
#     for i in range (a,b+1,1):
#         print(i)

# a = int(input("Enter a number"))
# b = int(input("Enter a number"))

# print_numbers(a,b)

# 2.SUM 
# Write a function to print all numbers from b to a in reverse order using a loop.
# def print_reverse(b, a):
#     # write your code here
# print_reverse(10, 5)
# print_reverse(7, 1)
# print_reverse(20, 15)

# def print_reverse(b, a):
#     for i in range (b,a-1,-1):
#         print(i)

# a=int(input("Enter a value:" ))
# b=int(input("Enter b value:" ))

# print_reverse(a,b)

# 3. SUM
# Write a function to print all numbers between a and b that are divisible by a given number n.
# def print_divisible(a, b, n):
#     # write your code here
# print_divisible(1, 20, 3)
# print_divisible(10, 30, 5)
# print_divisible(5, 25, 7)

# def print_divisible(a, b, n):
#     for i in range (a,b+1,1):
#         if i % n == 0:
#             print(i)

# a=int(input("Enter the a value :"))   
# b=int(input("Enter the b value:" ))   
# n=int(input("Enter the n value: "))

# print_divisible(a,b,n)


# 4.SUM
# Write a function to print all odd numbers between a and b in reverse order using a loop.
# def print_odd_reverse(a, b):
#     # write your code here
# print_odd_reverse(1, 10)
# print_odd_reverse(5, 15)
# print_odd_reverse(10, 20)

# def print_odd_reverse(a, b):
#     for i in range(b,a,-1):
#         if i % 2 != 0:
#             print(i)


# a=int(input("Enter the a value :"))   
# b=int(input("Enter the b value:" ))  

# print_odd_reverse(a,b)

# Write a function to count how many odd numbers are between a and b.
# def count_odd(a, b):
#     # write your code here
# count_odd(1, 10)
# count_odd(5, 20)
# count_odd(10, 15)

# def count_odd(a, b):
#  count=0
#  for i in range(a, b + 1,1):
#     if i % 2 != 0:
#         count=count+1
#  print(count)

# a=int(input("Enter the a value :"))   
# b=int(input("Enter the b value:" ))  


# Write a function to count how many numbers are divisible by a given number between a and b.
# def count_divisible(a, b, n):
#     # write your code here
# count_divisible(1, 10, 2)
# count_divisible(5, 25, 3)
# count_divisible(10, 50, 5)

# def count_divisible(a, b, n):
#     count=0
#     for i in range(a,b+1,1):
#         if i % n == 0:
#             count=count+1
#     print(count)        


# a=int(input("Enter the a value :"))   
# b=int(input("Enter the b value:" ))   
# n=int(input("Enter the n value: "))

# count_divisible(a,b,n)

# Write a function to find the sum of all numbers from a to b using a loop.
# def sum_range(a, b):
#     # write your code here
# sum_range(1, 5)
# sum_range(3, 7)
# sum_range(10, 12)

# def sum_range(a, b):
#     sum=0
#     for i in range(a,b+1,1):
#         sum=sum+i
#     print(sum)

# a=int(input("Enter the a value :"))   
# b=int(input("Enter the b value:" )) 

# sum_range(a,b)

# Write a function to find the sum of numbers from 1 to n.
# def sum_to_n(n):
#     # write your code here
# sum_to_n(5)
# sum_to_n(10)
# sum_to_n(3)

# def sum_to_n(n):
#     for i in range(1,n+1,1):
#         print(i)

# n=int(input("Enter the value of n :"))

# sum_to_n(n)


# Write a function to calculate taxi fare based on the following rates:
# First 10 km → ₹15/km
# Next 20 km → ₹12/km
# Beyond 30 km → ₹10/km
# def taxi_fare(distance):
#     # write your code here
# taxi_fare(10)
# taxi_fare(15)
# taxi_fare(35)

def taxi_fare(kms):
    if kms > 0 and kms < 10:
        fare=kms * 15
        print(fare)
    elif kms >10 and kms <= 20 :
        fare=(10*15)+(kms-10)*12
        print(fare)
    elif kms > 20 and kms <= 30 :
        fare=(10*15)+(20*12)+(kms-30)*10
        print(fare)
    else:
        print("Invalid Input")

kms=int(input("Enter the kms :"))

taxi_fare(kms)


# Write a function to find how many un-popped balloons remain after n balloons are inflated.
#  Every 4th balloon pops automatically.
# def balloons_left(n):
#     # write your code here
# balloons_left(4)
# balloons_left(10)
# balloons_left(20)

# balloon=int(input("Enter the number of balloon: "))
# popped = balloon // 4
# un_popped =  balloon -popped
# print("Popped Balloon",popped)
# print("Un Popped Balloon",un_popped)

balloon=int(input("Enter the number of balloon: "))

for_1000 = balloon // 1000 * 5
for_5000 = balloon // 5000 * 20

total = for_1000 + for_5000
print(total)



# n = int(input("enter months"))
# saving = 100
# total = 0
# for i in range(1,n+1):
#     total += saving
#     saving += 50
# print("Total savings after", n, "month is",total


n=int(input("Enter the number of month:"))
savings=100
total=0
for i in range(1,n+1):
    total+=savings
    savings