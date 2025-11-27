# # <!-- Level 3 Problems on Lists:
# # ### LISTS
# # - Given a list, rotate it right by k positions.
# # ```python
# # #test case 1:
# # Input: nums = [4,6,9,2,3,11], k = 2
# # Output: [3,11,4,6,9,2]
# # ```
# # - You are given a list of numbers and a target value.
# #   Your task is to find all the indices at which the target value appears and PUT THOSE IN A NEW LIST.
# # ```python
# # #test case 1
# # Input: nums = [4,2,7,2,9,3,2,8], k = 2
# # Output: [1,3,6]
# # #test case 2
# # Input: nums = [10,55,17,29,3], k = -45
# # Output: "Not Found"
# # ```
# # - Given a list of numbers, print the list in reverse order without using list slicing ([::-1]).
# # ```python
# # # test case 1
# # Input: nums = [1,3,7,8,9]
# # Output: [9,8,7,3,1]
# # # test case 2
# # Input: nums = []
# # Output: []
# # ```
# # ### STRINGS
# # - Write a program that takes a string as input and counts the number of uppercase letters in it.
# # ```python
# # # test case 1
# # Input: "HelloWorld"
# # Output: 2
# # # explanation -> H , W are upper case so, output is 2
# # ```
# # - Write a program that finds the longest word in a given sentence.
# #   (Bonus: If you are too studious, try without using `split(" ")` and solve)
# # ```python
# # # test case 1
# # Input: "Johannesburg is the most populous city of South Africa"
# # Output: "Johannesburg"
# # # based on the word length -> it is Johannesburg
# # ```
# # - Given a sentence, interchange the words that appear before and after every occurrence of the word `and`. The word `and` should remain in the same position, but the surrounding words must be swapped.
# # ```python
# # Input: apple and banana
# # Output: banana and apple
# # ``` -->

# def rotate_right(nums, k):
#     k = k % len(nums)
#     return nums[-k:] + nums[:-k]
# nums = [4,6,9,2,3,11]
# k = 2
# print(rotate_right(nums, k))


# nums = [4,2,7,2,9,3,2,8]
# k = 2
# res=[]
# for i in range(len(nums)):
#     if k == nums[i]:
#         res.append(i)
# print(res)



# number= [1,3,7,8,9]

# rev = []
# for i in range(len(number)-1, -1, -1):  
#     rev.append(number[i])

# print(rev)

# st="Hello WorlD"
# count=0
# for i in range(len(st)):
#     if st[i] >='A' and  st[i] <= 'Z':
#         count+=1
# print(count)


# s="Johannesburg is the most populous city of South Africa"
# space=s.split(" ")
# long_count=len(space[0])
# long_word=space[0]
# for i in range(len(space)):
#     if len(space[i]) > long_count:
#         long_count=len(space[i])
#         long_word=space[i]
# print(long_word)



# # Find the smallest word in a sentence.
# # Input: "Python is super powerful"
# # Output: is
# # 2. A list is strictly increasing if every next element is greater than the previous one.
# # Example:
# # [1,3,5,9] → True
# # [2,2,5] → False (because 2 is NOT less than 2)
# # [10,5,6] → False (because 5 < 10)
# # 3. Reverse characters only at even index positions Indices: 0,2,4,6,...
# # Input: "abcdefg" Even positioned letters: a, c, e, g → reverse → g, e, c, a
# # Final Output: "gbecdfa"
# # 4. Replace characters at odd indexes with *.
# # Example: "hello" → "h*l*o" (edited)


# s = "Python is super powerful"
# space = s.split(" ")

# small_word = space[0]
# small_count = len(space[0])




# for i in range( len(space)):
#     if len(space[i]) < small_count:
#         small_count = len(space[i])
#         small_word = space[i]

# print(small_word)


#   rev=""
#     for i in range(len(word)):
#         if i % 2 != 0:
#             rev = word[i]+rev
#             print(res)
def find_first_occurence(arr,value):
    first_value=0
    for i in range(len(arr)):
        if arr[i] == value:
            first_value=i
            break
    print(first_value)
find_first_occurence([9, 7, 4, 1, 7, 0], 9)