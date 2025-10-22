day=int(input("Enter the day:"))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day")
        


month=int(input("Enter the month:"))
match month:
    case 1:
        print("Jan")
    case 2:
        print("Feb")
    case 3:
        print("Mar")
    case 4:
        print("Apr")
    case 5:
        print("May")
    case 6:
        print("Jun")
    case 7:
        print("Jul")
    case 8:
        print("Aug")
    case 9:
        print("Sep")
    case 10:
        print("Oct")
    case 11:
        print("Nov")
    case 12:
        print("Dec")
    case _:
        print("Invalid month")



number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")
match operator:
        case '+':
            print(number1 + number2)
        case '-':
            print(number1 - number2)
        case '*':
            print(number1 * number2)
        case '/':
            print(number1 / number2)
        case _:
            print("invalid operator")


n=int(input("Enter the first number:"))
l=int(input("Enter the second number:"))
r=int(input("Enter the third number:"))
if n > l and n < r:
        print("yes")
else:
        print("no")

a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
c=int(input("Enter the value of c:"))
if(a > b and a > c):
    print(a)
elif (b > a and b > c):
    print(b)
else:
    print(c)






