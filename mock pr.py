num=int(input("Enter the number:"))
if num>0:
    print("The number is positive")
elif num==0:
    print("The number is zero")
else:
    print("The number is negative")



char=input("Enter the character :")
if char=="A" or "a":
    print("vowel")
elif char=="E" or "e":
    print("vowel")
elif char=="I" or "i":
    print("vowel")
elif char=="O" or "o":
    print("vowel")
elif char=="U" or "u":
    print("vowel")
else:
    print("consonant")

    
customer = float(input("Enter your amount"))
member = input("are you member say yes or no")
if  member == "yes":
    print(int(customer//10))
else:
    print("point:",0)