# You are given two strings.
#  Your task is to check whether the strings differ by exactly one character.
#  This means:
# Both strings must be of the same length


# Exactly one position must have different characters


# All other characters must be identical


# If the condition is satisfied, print "yes".
#  Otherwise, print "no".
# Testcase 1:
# Input:  s1 = "coding", s2 = "coting"
# Output: "yes"
# Testcase 2:
# Input: s1 = "apple", s2 = "abble"
# Output: "no"

# def different_by_one(s1,s2):
#     diff=0
#     if len(s1) != len(s2):
#          print("No")
#     for i in range(len(s1)):
#         if s1[i] != s2[i]:
#             diff+=1

#     if diff == 1:
#         print("yes")
#     else:
#         print("No")

# s1=input("Enter the string:")
# s2=input("Enter the string:")
# different_by_one(s1,s2)


# 2. Given two arrays:
# names → list of student names


# birthdates → list of dates in "dd/mm" format


# Write a program that prints the names of students who were born between January and June (inclusive).
# Use split() to extract day and month.
# Solution:

# def born_in_first_half(names, birthdates):
#     result = []
    
#     for i in range(len(names)):
#         day, month = birthdates[i].split("/")   # Split dd/mm
        
#         day = int(day)
#         month = int(month)

#         # Months 1 to 5 are fully included
#         # Month 6 → only dates from 1 to 30
#         if (1 <= month <= 5) or (month == 6 and day <= 30):
#             result.append(names[i])
    
#     print(result)


# Sample test case

# names = ["Arun", "Bala", "Cathy", "David", "Elena", "Farhan", "Gita", "Hari"]
# birthdates = ["05/01", "19/07", "23/03", "30/06", "11/11", "02/05", "15/06", "01/12"]

# born_in_first_half(names, birthdates)

# Output: 
# ['Arun', 'Cathy', 'David', 'Farhan', 'Gita']


def first_half_month(names,birthdates):
    result=[]
    for i in range(len(names)):
        day,month=birthdates[i].split("/")
        day=int(day)
        month=int(month)

        if( 1 <= month <= 5) or (month==6 and day <=31):
            result.append(names[i])
    print(result)


names = ["Arun", "Bala", "Cathy", "David", "Elena", "Farhan", "Gita", "Hari"]
birthdates = ["05/01", "19/07", "23/03", "30/06", "11/11", "02/05", "15/06", "01/12"]

first_half_month(names,birthdates)


# 3. An organization named "Higginbothams" maintains a library where all books with unique serial numbers are arranged in strict descending order (largest to smallest).
# A new book arrives with a unique serial number. The librarian wants to insert it in the correct position so the order remains unchanged.

# Given:
# A list of integers representing book serial numbers (sorted in descending order)


# An integer representing the new book's serial number
# Input:
# Books = [98, 75, 60, 50, 40, 25]
# NewBook = 55

def book_place(books,newbook):
    position=0
    for i in range(len(books)):
        if books[i] > newbook:
            position = i
            break
    else:
        print("-1")

books = [98, 75, 60, 50, 40, 25]
newbook = 55
book_place(books,newbook)