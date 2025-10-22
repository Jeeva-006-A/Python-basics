
mark_1=int(input("Enter the mark 1:"))
mark_2=int(input("Enter the mark 2:"))
mark_3=int(input("Enter the mark 3:"))
if mark_1>40 and mark_2>40 and mark_3>40:
    print(" Promoted")
else:
    print("Not  Promoted")
    

weather=input("Enter today's weather:")
if weather=="rainy":
    print("Bring Umbrella")
else:
     print("No umbrella needed")



day = input("Enter a day of the week:")
if day == "saturday" or day == "sunday":
     print("Holiday")
else:
     print("Working day")