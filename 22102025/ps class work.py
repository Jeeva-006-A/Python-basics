# 1. Write a function to split a given string on hyphens (-) and display each substring on a new line.

sentences=str(input("Enter the sentences:"))
# with using in built function
words=sentences.split('-')
for word in words:
    print(word)


sentences=str(input("Enter the sentences:"))
word=""
# without using in built function
for ch in sentences:
    if ch == '-':
        print(word)
        word=""
    else:
        word += ch

if word != "":
    print(word)        


# 2. Write a Python program to reverse a given string in two ways:
# using built in function
sentences=str(input("Enter the sentences:"))
reversed_sentences=sentences[::-1]
print(reversed_sentences)

# 3. Write a Python program to count the number of consonants in a given string.

words=str(input("Enter the words:"))
count=0
for i in range(len(words)):
    if words[i] not in ['a','e','i','o','u',""]:
        count += 1
print(count)    


# 4.  Write a Python program to remove all spaces from a given string.
def remove_space(text):
    new_text = ""
    for char in text:
        if char != " ":
            new_text = new_text + char
    print(new_text)
remove_space("Python is awesome")

#5. Write a Python program that asks the user to enter a password and checks if it is strong.
password = input('Enter your password:')
if len(password) >= 8:
    special = "!@#$%^&*"
    for char in password:
        if char in special:
            print('Password is strong')
            break
    else:
        print('Password is not strong')
else:
    print('Please enter at least 8 characters')
            
        

        
    
             
