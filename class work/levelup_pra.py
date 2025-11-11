# 1 .Given an array nums and an integer K, remove the last K elements from the array and print the remaining elements.
# Test Case 1:
# Input : nums = [10, 20, 30, 40, 50]
# K = 2
# Output: [10, 20, 30]
# Test Case 2:
# Input: nums = [5, 15, 25]
# K = 5
# Output: Invalid Input


nums = [10, 20, 30, 40, 50]
K = 2
for i in range(len(nums)):
    if nums > k :
        




#   2. Given two lists, calculate the total count of odd numbers in each list. Print the list that contains the highest count of odd numbers. If the counts are the same, print "Odd counts are equal".
# Test Case 1:
# Input:
# data_x = [1, 2, 3, 4, 5, 6, 7]
# data_y = [11, 22, 33, 44, 55]
# Output: [1, 2, 3, 4, 5, 6, 7]

data_x = [1, 2, 3, 4, 5, 6, 7]
data_y = [11, 22, 33, 44, 55]
count_x=0
count_y=0
for i in range(len(data_x)):
    if i % 2 !=0:
        count_x+=1
for i in range(len(data_y)):
    if i % 2 !=0:
        count_y+=1
if count_x > count_y:
    print(data_x)        
elif count_y > count_y:
    print(count_y)
else:
    print("Both are Equal")


#  3. Given an integer N and an array of N integers, write a program to print all the integers that are divisible by their immediate previous integer in the array.
# Test Case 1:
# Input: [1, 2, 3, 6, 7]
# Output: [2, 6]
# Test Case 2:
# Input: [2, 4, 8, 16]
# Output: [4, 8, 16]
# Test Case 3:
# Input: [5, 7, 11, 13, 17]
# Output: [].

arr=[1, 2, 3, 6, 7]
new_arr=[]
for i in range(len(arr)):
    if arr[i] % arr[i-1] == 0:
        new_arr.append(arr[i])
print(new_arr)

arr=[2, 4, 8, 16]
new_arr=[]
for i in range(len(arr)):
    if arr[i] % arr[i-1] == 0:
        new_arr.append(arr[i])
print(new_arr)


arr=[5, 7, 11, 13, 17]
new_arr=[]
for i in range(len(arr)):
    if arr[i] % arr[i-1] == 0:
        new_arr.append(arr[i])
print(new_arr)











































































































































