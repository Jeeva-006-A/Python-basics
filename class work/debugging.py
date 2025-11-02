# # 1. There is an error while reversing the given string. Please identify and correct it.
# word = "Python"
# rev = ""
# for i in range(len(word)):
#     rev =  word[i] + rev 
# print("Reversed:", rev)

# # 2. There is an error while counting vowels in the given text. Please identify and correct it.
# text = "Education"
# count = 0
# for i in range(len(text)):
#         if text[i] in "aeiouAEIOU":
#              count += 1
# print("Vowels:", count)

# # 3. There is an error while finding the smallest element in the list. Please identify and correct it.
# nums = [9, 5, 3, 8]
# min_num = nums[0]
# for i in range(1, len(nums)):
#     if nums[i] < min_num:
#         min_num = nums[i]
# print("min_num:",min_num)

# # 4. There is an error while printing alternate elements from the list. Please identify and correct it.
# lst = [10, 20, 30, 40, 50]
# for i in range(0,len(lst)):
#     if i % 2 == 0:
#         print(lst[i])

# # 5. There is an error while replacing negative numbers in the list with 0. Please identify and correct it.
# nums = [-3, 5, -2, 7]
# for i in range(0,len(nums)):
#      if nums[i] < 0:
#           nums[i] = 0
#           print(nums)


# name=['Nathiya',]


# 1. There is an error while counting how many times a number appears in the list. Please identify and correct it.
nums = [1, 2, 3, 2, 2, 4]
target = 2
count = 0
for i in range(len(nums)):
    if nums[i] == target:
        count += 1
print(count)
# 2. There is an error while comparing two strings character by character. Please identify and correct it.
s1 = "cat"
s2 = "cat"
same = True
if s1 == s2:
    same = True
else:
    same = False
print("Same")
# else:
#     print("Different")
# 3. There is an error while counting spaces in a given sentence. Please identify and correct it.
# sentence = "Python is fun"
# spaces = 0
# for ch in sentence:
#     if ch == "":
#         spaces += 1
# print("Spaces:", spaces)
# 4. There is an error while finding the frequency of each character in a string. Please identify and correct it.
# text = "banana"
# for ch in text:
#     c = 0
#     for i in range(len(text)):
#         if text[i] == ch:
#             c = c + 1
#     print(ch, ":", c)
# 5. There is an error while counting the number of words in a given string. Please identify and correct it.
# text = "I love Python"
# count = 1
# for ch in text:
#     if ch == " ":
#         count = 0
# print("Words:", count)