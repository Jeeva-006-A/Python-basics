# 1 Sum Answer
# n=int(input("Enter the first number:"))
# m=int(input("Enter the second number:"))
# o=n+m
# if o % 2==0:
#   print("EVEN")
# else:
#    print("ODD")



# # 2 Sum Answer
# n=int(input("Enter the two digit number:"))
# a = n // 10
# b = n % 10
# m = a + b
# j = a * b
# if m + j == n :
#     print("Great")
# else:
#     print("Not Great")



# 3 Sum Answer
# c = input("What kind of consumer (residential/commercial):")
# u = int(input("Enter units : "))
# if c == "residential":
#     if u >= 0 and u <= 100:
#         print("Total unit amount is =", 3*u)
#     elif u > 100 and u <= 200:
#         print("Total unit amount is =", 5*u)
#     elif u > 200:
#         print("Total unit amount is =", 7*u)
# elif c == "commercial":
#     if u >= 0 and u <= 100:
#         print("Total unit amount is =", 3*u)
#     elif u > 100 and u <= 200:
#         print("Total unit amount is =", 7*u)
#     elif u > 200:
#         print("Total unit amount is =", 10*u)




# 4 Sum Answer
# o=int(input("Enter the km:"))
# if o <= 5:
#     fare = o * 10
#     # print("Distance fare =",o*10)
# elif o > 5 and 0 <= 15:
#     fare = o * 8
#     # print("Distance fare =",o*8)
# elif o > 15:
#     fare = o * 6
#     # print("Distance fare =",o*6)
# if fare < 50:
#     fare = 50
# print("The Final Fare =",fare)



# 5 Sum Answer
# a =int(input())
# b =int(input())
# c =int(input())

# if a+b > c and b+c > a and c+a > b:
#     if a == b and b == c and c == a:
#         print("It is a Equilateral  all three sides are equal")
#     elif a == b or b == c or c ==a :
#         print("It is a Isosceles  any two sides are equal")
#     elif a != b and b != c and c != b:
#         print("It is a Scalene all three sides are different")
# else:
#         print("Not a valid triangle")



# 6 Sum Answer
# a=int(input("Enter the number:"))
# if a % 3 == 0 and a % 5 == 0:
#     print("FizzBuzz")
# elif a % 3 == 0:
#     print("Fizz")
# elif a % 5 == 0:
#     print("Buzz")
# else:
#     print("Invalid")



# 7 Sum Answer
# a=(input("Enter the subject,Science/Commerce/Arts"))
# match a:
#     case"Science":
#         b=(input("Medical/Engineering"))
#         match b:
#             case"Medical":
#                 print("you choose Science in 'Medical'")
#             case"Engineering":
#                 print("you choose Science in 'Engineering'")
#             case _:
#                 print("Invalid")
#     case"Commerce":
#         c=(input("CA/B COM"))
#         match c:
#             case"CA":
#                 print("you choose Commerce in CA")
#             case"B COM":
#                 print("you choose Commerce in B COM")
#             case _:
#                 print("Invalid")
#     case"Arts":
#         d=(input("History / Literature"))
#         match d:
#             case"History":
#                 print("you choose Arts in History")
#             case"Literature":
#                 print("you choose Arts in Literature")
#             case _:
#                 print("Invalid")
#     case _:
#         print("Invalid Subject you entered")


                

# 8 Sum Answer               
# a=int(input("Enter the show timing :"))
# if a >= 9 and a <= 12:
#     print("Morning Show")
# elif a >= 12 and a <= 16:
#     print("Matinee Show")
# elif a >=16 and a<=16:
#       print("Evening Show")
# else:
#      print("night Show")




# 9 Sum Answer
# a=int(input("Enter the km"))
# b=int(input("M(1) or CM(2) or MM(3),MI(4)"))
# match b:
#     case 1:
#         print(a*1000)
#     case 2:
#         print(a*100000)
#     case 3:
#         print(a*1000000)
#     case 4:
#         print(a*0.621371)
#     case _:
#         print("Invalid Conversion")




# 10 Sum Answer
# payment_method=input("Enter the payment method,UPI/Cards/Net Banking/COD:")
# payment_method=payment_method.upper()
# if payment_method =="UPI":
#    print("You selected UPI payment")  
# elif payment_method =="Cards":
#    print("You selected Debit/Credit Cards payment")
# elif payment_method =="Net Banking":
#    print("You selected Net Banking")
# elif payment_method =="COD":
#    print("You selected Cash On Delivery")
# else:
#    print("Invalid Payment Mode")   

# n=int(input("Enter the two digit number:"))
# a=n//10
# b=n%10
# m=a+b
# j=a*b

          
