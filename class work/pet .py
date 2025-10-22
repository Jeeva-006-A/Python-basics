# a=int(input("Enter the Year:"))
# if a%4==0 and a%100 !=0:
#     print("Y")
# elif a%400 ==0:
#     print("Y")
# else:
#     print("N")

a=int(input("Enter the a value:"))
b=int(input("Enter the b value:"))
sum=0
i=a
while i<=b:
    if i %2==0:
        sum_even +=i
    i+=1 
print("Sum of even numbers:",sum_even)