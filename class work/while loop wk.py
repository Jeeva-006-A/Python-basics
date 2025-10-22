# 1 Sum Answer:
# number=0
# while number <= 100:
#     if number % 5==0:
#         print(number)
#         number=number+5

# 2 Sum Answer
# number = int(input("Enter a number: "))
# i = 1
# while i <= 10:
#     print(number, "x", i, "=", number * i)
#     i += 1
    

# 3 Sum Answer
# i = 1
# total = 0

# while i <= 5:
#     total = total + i
#     i += 1

# print("Sum =", total)



# number=int(input("Enter a number:"))
# i=1
# while i <= number:
#     print("cube of",i,"=",i**3)
#     i+=1
    
# start=int(input("Enter the stating number:"))
# count=int(input("Enter how many number to print:"))
# i=0
# while  i < count:
#     print(start+i)
#     i+=1
    

# number=int(input("Enter the number of terms:"))
# i=1
# while i <= number:
#     term=i**2+1
#     print(term)
#     i+=1


n=int(input("Enter the number:"))
if n<=0:
    print("Invalid Input")
i=1
while i <= n:
    print(i*i)
    i=i+i